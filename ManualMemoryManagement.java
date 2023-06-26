/*
 * Manual Memory is a very interesting & powerful technique in CS.
 * This code snippet is a demonstration of manual memory management
 * in java. One way to achieve it is by native code through JNI 
 * (Java Native Interface https://www.baeldung.com/jni) or using
 * direct byte buffers. Here following code makes use of 'java.nio'
 * package which contains classes like ByteBuffer & DirectByteBuffer
 * which allows manual memory management through explicit allocation
 * & deallocation of native memory blocks.
 */
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
public class ManualMemoryManagement {
    public static void main(String[] args) {
        // Allocate native memory block of size 1KB
        int bufferSize = 1024;
        ByteBuffer buffer = ByteBuffer.allocateDirect(bufferSize);
        String name = "Tejas";
        // Put the name "Tejas" into the buffer
        buffer.put(name.getBytes(StandardCharsets.UTF_8));
        // Flip the buffer to prepare for reading
        buffer.flip();
        // Read the name from the buffer and convert it back to a String
        byte[] nameBytes = new byte[name.length()];
        buffer.get(nameBytes);
        String extractedName = new String(nameBytes, StandardCharsets.UTF_8);
        // Print the extracted name
        System.out.println("Name: " + extractedName);
        // Clear the buffer to make it ready for reuse
        buffer.clear();
    }
}