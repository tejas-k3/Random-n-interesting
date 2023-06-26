// This is an exciting piece of web3 code which has a simple decentralized
// application (dApp) backend and a smart contract written in Solidity which
// is used for developing contracts on Ethereum blockchain.
pragma solidity ^0.8.0;

// A basic contract without real-world complexities only having get & set 
// method for ease of understanding.
contract SimpleStorage {
    uint256 private storedData;
    function set(uint256 newValue) public {
        storedData = newValue;
    }
    function get() public view returns (uint256) {
        return storedData;
    }
}

// This contract acts as a backend logic for a hypothetical app intracting with 
// SimpleStorage contract by deploying it and using its functions. The constructor
// is called  when deploying the SimpleDapp contract and takes the address of the
// deployed SimpleStorage contract as an argument.
contract SimpleDapp {
    SimpleStorage private storageContract;
    constructor(address storageContractAddress) {
        storageContract = SimpleStorage(storageContractAddress);
    }
    function updateStoredData(uint256 newValue) public {
        storageContract.set(newValue);
    }
    function getStoredData() public view returns (uint256) {
        return storageContract.get();
    }
}
