"""
RaftNode Class:
* Each node maintains its state (follower, candidate, leader).
* It tracks the current term and the node it voted for.
* The log stores commands, and commit_index tracks the last committed entry.

Leader Election:
* A node starts an election by incrementing its term and voting for itself.
* It requests votes from peers and becomes the leader if it receives a majority.

Log Replication:
* The leader appends entries to its log and simulates sending them to followers.
* Followers replicate these entries in their logs.

Heartbeats:
* The leader periodically sends heartbeats to maintain its leadership.
* Followers reset their election timeouts upon receiving a heartbeat.

Limitations of This code is it simplifies many aspects of Raft for clarity:
* It doesn't handle log persistence or network failures.
* It lacks a mechanism for applying log entries to a state machine.
* It uses a simple voting mechanism without considering network partitions.

Real-World Implementations
Real-world Raft implementations, like etcd or ZooKeeper, handle these complexities and provide robust distributed systems for managing configuration data or distributed locks.
"""
import random
import time
import threading

class RaftNode:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.state = "follower"
        self.current_term = 0
        self.voted_for = None
        self.log = []
        self.commit_index = 0
        self.last_applied = 0
        self.election_timeout = random.randint(150, 300)  # in milliseconds

    def start_election(self):
        self.current_term += 1
        self.voted_for = self.node_id
        votes = 1  # Vote for itself
        for peer in self.peers:
            if peer.vote_for(self.node_id, self.current_term):
                votes += 1
        if votes > len(self.peers) / 2:
            self.state = "leader"
            print(f"Node {self.node_id} became leader.")
            self.start_leader()

    def vote_for(self, candidate_id, term):
        if term > self.current_term:
            self.current_term = term
            self.voted_for = candidate_id
            return True
        return False

    def start_leader(self):
        # Simulate sending heartbeats to followers
        while self.state == "leader":
            for peer in self.peers:
                peer.receive_heartbeat(self.node_id, self.current_term)
            time.sleep(0.1)

    def receive_heartbeat(self, leader_id, term):
        if term >= self.current_term:
            self.current_term = term
            self.state = "follower"
            self.election_timeout = random.randint(150, 300)  # Reset election timeout

    def append_to_log(self, entry):
        self.log.append(entry)
        # Simulate log replication
        for peer in self.peers:
            peer.replicate_log(entry)

    def replicate_log(self, entry):
        self.log.append(entry)

if __name__ == "__main__":
    nodes = [RaftNode(i, []) for i in range(5)]
    for i, node in enumerate(nodes):
        node.peers = [n for j, n in enumerate(nodes) if j != i]

    # Start election for each node
    threads = []
    for node in nodes:
        t = threading.Thread(target=node.start_election)
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()
