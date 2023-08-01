"""
Synchronous Approach with Threading:
Uses multiple threads to achieve concurrency.
Limited by the Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time.
Suitable for I/O-bound tasks where threads can switch while waiting for I/O operations.

Asynchronous Approach with async and await:
Uses asyncio and async/await to achieve concurrency.
Handles I/O-bound tasks efficiently without the need for multiple threads.
More suitable for handling a large number of concurrent I/O operations without the GIL limitation.
"""

import asyncio
import threading

class PortAllocator:
    def __init__(self):
        self.allocated_ports = set()
        self.lock = threading.Lock()

    def allocate_sync(self):
        with self.lock:
            for port in range(1025):
                if port not in self.allocated_ports:
                    self.allocated_ports.add(port)
                    return port
            raise Exception("No free ports available.")

    def deallocate_sync(self, port):
        with self.lock:
            if port in self.allocated_ports:
                self.allocated_ports.remove(port)
            else:
                raise Exception("Port is not allocated or already deallocated.")

    async def allocate_async(self):
        for port in range(1025):
            if port not in self.allocated_ports:
                self.allocated_ports.add(port)
                return port
        raise Exception("No free ports available.")

    async def deallocate_async(self, port):
        if port in self.allocated_ports:
            self.allocated_ports.remove(port)
        else:
            raise Exception("Port is not allocated or already deallocated.")


def user_task_sync(allocator, user_id):
    try:
        port = allocator.allocate_sync()
        print(f"User {user_id} got port: {port}")
        allocator.deallocate_sync(port)
        print(f"User {user_id} released port: {port}")
    except Exception as e:
        print(f"User {user_id} encountered an error: {e}")


async def user_task_async(allocator, user_id):
    try:
        port = await allocator.allocate_async()
        print(f"User {user_id} got port: {port}")
        await asyncio.sleep(1)  # Simulating some asynchronous work
        await allocator.deallocate_async(port)
        print(f"User {user_id} released port: {port}")
    except Exception as e:
        print(f"User {user_id} encountered an error: {e}")


def main():
    allocator_sync = PortAllocator()
    allocator_async = PortAllocator()

    # Using synchronous approach with threading
    threads = []
    for i in range(3):
        thread = threading.Thread(target=user_task_sync, args=(allocator_sync, i))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # Using async-await approach with asyncio
    asyncio.run(async_main(allocator_async))


async def async_main(allocator):
    tasks = [user_task_async(allocator, i) for i in range(3)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    main()
