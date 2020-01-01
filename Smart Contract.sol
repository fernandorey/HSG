    //We select the version the compiler. We use one of the latest releases, Solidity ^0.5.1
    pragma solidity ^0.5.1;

    //we start the contract
    contract MyContract {
        //this will be our contract list. Is a public int that count how many contracts we have. We start at 100 is the INDEX
        //of the first contract.
        uint256 public contractCounter = 100;
        //Solidity uses mapping structure value types, such as booleans, integers, addresses, and structs. It consists of two main parts: a _KeyType and a _ValueType.
        //We create a mapping structure of Struct Ob
        mapping (uint => ObjectContract) public contractList;
        //We create the Struct that will hold the Information to be saved in the Blockchain (Object / Type Contract) 
        struct ObjectContract {
            uint contractNumber;
            string _name;
            string _email;
            string _hash;
        }
        
        //By this function we add one new CONTRACT to the list. We add name / email / hash and we use the Contract Counter.
        function newContract(string memory _name  , string memory _email, string memory _hash) public {
            contractCounter = contractCounter + 1;
            contractList[contractCounter] = ObjectContract(contractCounter, _name, _email,_hash);
        }
        

        //By this function we search for the HASH in the list.
        function searchContract(string memory _search) view public returns (uint256) {
            //We loop searching threw the entire contractList
            for(uint256 i=99 ; i < contractCounter + 1  ; i++) {
                //In soloidity strings can't be compared, so we HASH them and compare hashes. 
                if(keccak256(abi.encodePacked(_search)) == keccak256(abi.encodePacked(contractList[i]._hash))) {
                    return i;
                }

            } 
        }
        
        //We retrive the entire registry from the contractList, using the index.  
        function viewContract(uint256 _num) view public returns (uint256, string memory, string memory, string memory) {
            return (contractList[_num].contractNumber, contractList[_num]._name, contractList[_num]._email, contractList[_num]._hash); 
        }
        
        //Returns how many contract exists, this is in order to loop in the python program.   
        function countContracts() view public returns (uint256) {
            return contractCounter; 
        }
    }