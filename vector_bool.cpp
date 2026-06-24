/*
vector<bool> looks like a normal vector of bool values, but it is not a
regular std::vector<T> specialization. It is a special optimized version
that usually stores boolean values as packed bits instead of storing each
value as a full bool object. This saves memory, but changes behavior in
ways that are often surprising in generic code.

What it should be:
A normal vector specialization should behave like other vectors. That means
operator[] should return a real reference to the stored element, address-of
should work naturally, and the container should feel identical to
vector<int>, vector<char>, etc.

What it is:
vector<bool> is a specialized container with bit-packing behavior. Since a
single bit cannot be referenced like a real object in memory, element access
commonly returns a proxy object instead of bool&. So although it acts like a
container of boolean values at a high level, it does not behave like a true
vector<bool> in the same way vector<int> behaves like a true vector<int>.

Why this matters:
Because of proxy references and packed storage, code that expects normal
reference semantics can break. This affects templated code, pointer usage,
address-taking, and sometimes performance assumptions. Memory efficiency is
gained, but regular container behavior is weakened.

Impact:
1. Saves memory for large boolean collections.
2. Does not provide normal bool& semantics.
3. Can confuse generic code and STL-style expectations.
4. May introduce subtle bugs when code assumes real references.
5. Often avoided unless bit-packing is specifically useful.

Practical recommendation:
Use vector<bool> only when compact storage is genuinely important. If normal
container behavior is preferred, use vector<char>, vector<uint8_t>, or a
more explicit bit-oriented structure depending on the use case.
*/

#include <iostream>
#include <type_traits>
#include <vector>

using namespace std;

/*
Example 1:
This example shows that reading from vector<bool> looks normal, but the type
returned by operator[] is usually not bool. Instead, it is a proxy object
that can convert to bool.
*/
void proxy_read_demo() {
    vector<bool> flags = {true, false, true};

    auto x = flags[0];
    bool y = flags[0];

    cout << boolalpha;
    cout << "flags[0] as bool value = " << y << '\n';
    cout << "is decltype(flags[0]) actually bool? "
         << is_same_v<decltype(flags[0]), bool> << '\n';
    cout << "is decltype(y) actually bool? "
         << is_same_v<decltype(y), bool> << '\n';
}

/*
Example 2:
A normal vector returns a real reference from operator[]. That means the code
below is valid for vector<int>. This is the expected vector-like behavior.
*/
void normal_vector_demo() {
    vector<int> nums = {10, 20, 30};
    int& ref = nums[0];
    ref = 99;

    cout << "nums[0] after modifying through int& = " << nums[0] << '\n';
}

/*
Example 3:
The same style does not work naturally with vector<bool> because operator[]
does not provide a real bool& in typical implementations.

The commented line below is intentionally left as reference. In real-world
compilers, trying to bind bool& to flags[0] fails because flags[0] is a proxy
object, not a real bool lvalue.
*/
void vector_bool_reference_demo() {
    vector<bool> flags = {true, false, true};

    // bool& ref = flags[0]; // Not valid: flags[0] is usually a proxy, not bool&
    auto proxy = flags[0];
    proxy = false;

    cout << "flags[0] after proxy assignment = " << flags[0] << '\n';
}

/*
Example 4:
This shows a behavioral difference that matters in generic code. A template
or helper that assumes T& semantics may work for most vector<T> cases but can
fail or require special handling for vector<bool>.
*/
template <typename T>
void flip_first(vector<T>& data) {
    T& ref = data[0];
    ref = !ref;
}

/*
The template above works for vector<int> or vector<char> in a type-correct
sense if the operations are meaningful, but it does not work for vector<bool>
in the same way because data[0] is not a real bool&.

A vector<bool>-safe version reads and writes via value semantics instead of
assuming reference semantics.
*/
void flip_first_bool_safe(vector<bool>& data) {
    bool value = data[0];
    data[0] = !value;
}

int main() {
    cout << "--- proxy_read_demo ---\n";
    proxy_read_demo();

    cout << "\n--- normal_vector_demo ---\n";
    normal_vector_demo();

    cout << "\n--- vector_bool_reference_demo ---\n";
    vector_bool_reference_demo();

    cout << "\n--- flip_first_bool_safe ---\n";
    vector<bool> flags = {true, false, true};
    flip_first_bool_safe(flags);
    cout << "flags[0] after safe flip = " << flags[0] << '\n';

    return 0;
}
