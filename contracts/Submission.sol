pragma solidity ^0.5.0;


import "./DateTime.sol";

/**
 * The submission contract accepts farmer input and displays their details
 */
contract Submission {
  constructor() public {
    _cropSubmission("mango", 12, 35);
  }

  event cropSubmitted(string name, uint quantity, uint quality, uint dateOfHarvest, uint cropId);

  struct Crop {
  	string name;
  	uint quantity;
  	uint quality;
  	uint dateOfSubmission;
  }

  Crop[] public crops;

  mapping (uint => address) public cropToOwner;
  
  function _cropSubmission(string memory _name, uint _quantity, uint _quality) public {
    uint _dateOfHarvest = now;
  	uint id = crops.push(Crop(_name, _quantity, _quality, _dateOfHarvest));
  	cropToOwner[id] = msg.sender;
  	//notify created crop
  	emit cropSubmitted(_name, _quantity, _quality, _dateOfHarvest, id);
  }

}

