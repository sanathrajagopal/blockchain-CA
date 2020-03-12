pragma solidity ^0.4.0;

contract Publish_Public_Key {
    //Contract to facilitate sending of public key to this smart contract
    
    //dict of addresses allowed to publish the public key
    mapping(address => bool) approvedPublisher;
    //dict of public key for each address
    mapping(address => string) pubkey;
    
    //event to announce the public key on the blockchain
    event PublicKeyPublish(address _publisher, string _publickey);
    
    constructor() public {}
    
    //payable function, will be called when ether is sent to the contract
    function() public payable{}
    
    function ApprovePublisher(address _publisher) public returns (bool success) {
        if(msg.sender == address(0x29CA6bDd9FDf408dc5b8dAC5a0b62a92fb06f975)) {
            approvedPublisher[_publisher] = true;
            return true;
        }
    }
    
    //read only function to check if the publisher is an approved publisher
    function isApproved(address _publisher) public view returns (bool approved) {
        return approvedPublisher[_publisher];
    }
    
    //read only function to get the current public key
    function get_pubkey(address _publisher) public view returns(string) {
        return pubkey[_publisher];
    }
    
    //function to modify the state on the blockchain
    function broadcastPublicKey(string _publickey, address _publisher) public returns (bool success) {
        if(approvedPublisher[_publisher] && (msg.sender == address(0x29CA6bDd9FDf408dc5b8dAC5a0b62a92fb06f975) || msg.sender == _publisher)) {
            pubkey[_publisher] = _publickey;
            emit PublicKeyPublish(_publisher,pubkey[_publisher]);
            return true;
        }
        else {
            return false;
        }
    }
    
}