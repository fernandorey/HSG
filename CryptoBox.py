#We use tkinter library as Graphical User Interfaces, in order to make the user select the file to FingerPrint. 
import tkinter as tk
from tkinter import filedialog
#Hashlib is used in order to calculate MD5 hash of the selected file (What we are saving in ) 
import hashlib
#We use Json library in order to use Javascript Object Notation, the list of commands defined as "ABI" define the properties and commands of the Smart Conctact 
import json
#We use Web3 as the library that allows us to interact with the Ethereum Blockchain. 
from web3 import Web3
#We use this library to clear the screen --> os.system ("cls")
import os

#We use Ganache, an Etherum development to deploy contracts and run tests  In order to run the programm, ganache has to be download and open  
#in the computer. The user need to update the line:address = web3.toChecksumAddress(""), writing the first addres shown on ganache.
#https://www.trufflesuite.com/ganache
#update this link with the URL of your computer. 
ganache_url = "HTTP://127.0.0.1:7545"

# Initialising a Web3 instance with an RPCProvider (GANACHE in this case)
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]

#Here we list the funcions of the contract Application Binary Interface (ABI). Is the standard way to interact with contracts in the Ethereum ecosystem,
abi = json.loads('[{"constant":true,"inputs":[],"name":"contractCounter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"contractList","outputs":[{"internalType":"uint256","name":"contractNumber","type":"uint256"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_email","type":"string"},{"internalType":"string","name":"_hash","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"countContracts","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_email","type":"string"},{"internalType":"string","name":"_hash","type":"string"}],"name":"newContract","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"string","name":"_search","type":"string"}],"name":"searchContract","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_num","type":"uint256"}],"name":"viewContract","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')


#We set the bytecode of the complete smart contract generated in Solidity, in order to be deployed.
bytecode = "6080604052606460005534801561001557600080fd5b50610d70806100256000396000f3fe608060405234801561001057600080fd5b50600436106100625760003560e01c8063067bd3b4146100675780636a5bb5d814610085578063b17dc3ab1461020b578063dfff292014610229578063feb3f929146103af578063ff3a3afe1461047e575b600080fd5b61006f610667565b6040518082815260200191505060405180910390f35b6100b16004803603602081101561009b57600080fd5b810190808035906020019092919050505061066d565b60405180858152602001806020018060200180602001848103845287818151815260200191508051906020019080838360005b838110156100ff5780820151818401526020810190506100e4565b50505050905090810190601f16801561012c5780820380516001836020036101000a031916815260200191505b50848103835286818151815260200191508051906020019080838360005b8381101561016557808201518184015260208101905061014a565b50505050905090810190601f1680156101925780820380516001836020036101000a031916815260200191505b50848103825285818151815260200191508051906020019080838360005b838110156101cb5780820151818401526020810190506101b0565b50505050905090810190601f1680156101f85780820380516001836020036101000a031916815260200191505b5097505050505050505060405180910390f35b610213610865565b6040518082815260200191505060405180910390f35b6102556004803603602081101561023f57600080fd5b810190808035906020019092919050505061086e565b60405180858152602001806020018060200180602001848103845287818151815260200191508051906020019080838360005b838110156102a3578082015181840152602081019050610288565b50505050905090810190601f1680156102d05780820380516001836020036101000a031916815260200191505b50848103835286818151815260200191508051906020019080838360005b838110156103095780820151818401526020810190506102ee565b50505050905090810190601f1680156103365780820380516001836020036101000a031916815260200191505b50848103825285818151815260200191508051906020019080838360005b8381101561036f578082015181840152602081019050610354565b50505050905090810190601f16801561039c5780820380516001836020036101000a031916815260200191505b5097505050505050505060405180910390f35b610468600480360360208110156103c557600080fd5b81019080803590602001906401000000008111156103e257600080fd5b8201836020820111156103f457600080fd5b8035906020019184600183028401116401000000008311171561041657600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610ab1565b6040518082815260200191505060405180910390f35b6106656004803603606081101561049457600080fd5b81019080803590602001906401000000008111156104b157600080fd5b8201836020820111156104c357600080fd5b803590602001918460018302840111640100000000831117156104e557600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192908035906020019064010000000081111561054857600080fd5b82018360208201111561055a57600080fd5b8035906020019184600183028401116401000000008311171561057c57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803590602001906401000000008111156105df57600080fd5b8201836020820111156105f157600080fd5b8035906020019184600183028401116401000000008311171561061357600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610bea565b005b60005481565b6001602052806000526040600020600091509050806000015490806001018054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561071f5780601f106106f45761010080835404028352916020019161071f565b820191906000526020600020905b81548152906001019060200180831161070257829003601f168201915b505050505090806002018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156107bd5780601f10610792576101008083540402835291602001916107bd565b820191906000526020600020905b8154815290600101906020018083116107a057829003601f168201915b505050505090806003018054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561085b5780601f106108305761010080835404028352916020019161085b565b820191906000526020600020905b81548152906001019060200180831161083e57829003601f168201915b5050505050905084565b60008054905090565b600060608060606001600086815260200190815260200160002060000154600160008781526020019081526020016000206001016001600088815260200190815260200160002060020160016000898152602001908152602001600020600301828054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156109635780601f1061093857610100808354040283529160200191610963565b820191906000526020600020905b81548152906001019060200180831161094657829003601f168201915b50505050509250818054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156109ff5780601f106109d4576101008083540402835291602001916109ff565b820191906000526020600020905b8154815290600101906020018083116109e257829003601f168201915b50505050509150808054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610a9b5780601f10610a7057610100808354040283529160200191610a9b565b820191906000526020600020905b815481529060010190602001808311610a7e57829003601f168201915b5050505050905093509350935093509193509193565b600080606390505b600160005401811015610be357600160008281526020019081526020016000206003016040516020018082805460018160011615610100020316600290048015610b3a5780601f10610b18576101008083540402835291820191610b3a565b820191906000526020600020905b815481529060010190602001808311610b26575b505091505060405160208183030381529060405280519060200120836040516020018082805190602001908083835b60208310610b8c5780518252602082019150602081019050602083039250610b69565b6001836020036101000a038019825116818451168082178552505050505050905001915050604051602081830303815290604052805190602001201415610bd65780915050610be5565b8080600101915050610ab9565b505b919050565b60016000540160008190555060405180608001604052806000548152602001848152602001838152602001828152506001600080548152602001908152602001600020600082015181600001556020820151816001019080519060200190610c53929190610c96565b506040820151816002019080519060200190610c70929190610c96565b506060820151816003019080519060200190610c8d929190610c96565b50905050505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10610cd757805160ff1916838001178555610d05565b82800160010185558215610d05579182015b82811115610d04578251825591602001919060010190610ce9565b5b509050610d129190610d16565b5090565b610d3891905b80821115610d34576000816000905550600101610d1c565b5090565b9056fea265627a7a7231582003ff8fab74afc9d806871688f504c9e3f3b0983b73b090689a47c90a2eca14d364736f6c634300050c0032"

#We select the addres that will execute the Smart Contract in order to run the transactions. 
address = web3.toChecksumAddress("0xe3aa467e29b00Dfa101756CAe8D986Cd1b902156")

#We deploy the SmartContract in the Ethereum Blockchain
Deploy = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = Deploy.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)


#This function calculates the MD5 Hash of the selected document. 
def getmd5file(archivo):
    hashmd5 = hashlib.md5()
    f = open(archivo, "rb")
    for bloque in iter(lambda: f.read(4096), b""):
        hashmd5.update(bloque)
    return hashmd5.hexdigest()
   
#This function launches the graphic interface for the user select the document he want to hash. 
def uploadfile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    #returns the filepath
    return(getmd5file(file_path)) 
    
#This function upload a new registry into the Blockchain. 
def option1():
    hasher = ""
    contractnumber = ""
    os.system ("cls")
    input("\n\nP<------------------------ Press ANY KEY to SELECT the file you want to hash in to the BLOCKCHAIN------------------------>")
    
    #upload function is called,it actually returns the MD5 HASH of the selected document.
    hasher = uploadfile()  
    print ("\n\nThe MD5 Hash of the document is %s." % hasher)
    name = input('\n\nPlease insert your full name: ')
    email = input('\n\nPlease insert your email: ')
    input("\n\n<------------------------ Press ANY KEY to save the information in to the BLOCKCHAIN------------------------>")    
    os.system ("cls")
    
    #Writes the information into the Ehtereum Blockchain.
    tx_hash = contract.functions.newContract(name, email, hasher).transact() 
    
    #wait untill the transaction es exectued, the block is mined, and the transaction confirmed.  
    web3.eth.waitForTransactionReceipt(tx_hash) 
    
    #In order to verify and get the number of register from the smart contract
    #we call "SEARCH CONTRACT", this function loops threw the entire registries 
    #until the saved hash is found 
    contractnumber = str(contract.functions.searchContract(hasher).call()) 

    print("\n\nThe contract was saved!\n\n "\
        "##############################################################################\n\n\n"\
        "         INDEX NUMBER: %s\n\n         NAME: %s\n\n         EMAIL: %s\n\n         HASH: %s\n\n\n"\
        "##############################################################################\n"\
        "         TRANSACTION RECEIPT: %s \n "\
        "##############################################################################\n\n\n"\
         % (contractnumber, name, email, hasher, tx_hash))
    input("<------------------------ Press ANY KEY to CONTINUE ------------------------>\n\n")

#This function looks for a specific saved contract and returns the information to the user.
def option2(): 
    os.system ("cls")
    referenceNumber = int(input("Please insert the reference number of the contract you want to verify: "))
    listReturn = []
    listReturn = contract.functions.viewContract(referenceNumber).call() 
    print("Request:\n\n "\
    "##############################################################################\n\n\n"\
    "         INDEX NUMBER: %s\n\n         NAME: %s\n\n         EMAIL: %s\n\n         HASH: %s\n\n\n"\
    "##############################################################################\n"\
    %   (str(listReturn[0]), listReturn[1], listReturn[2], listReturn[3]))
    input("<------------------------ Press ANY KEY to CONTINUE ------------------------>\n")

#This function return the list of existing documents saved.
def option3(): 
    os.system ("cls")
    contractnumber = contract.functions.countContracts().call()
    print( "List of existing contracts saved in Cryptobox: ")
    for x in range (101, contractnumber+1, 1):
        listReturn = []
        listReturn = contract.functions.viewContract(x).call() 
        print("##############################################################################\n"\
               "         INDEX NUMBER: %s ||        NAME: %s ||        EMAIL: %s ||        HASH: %s"\
               % (str(listReturn[0]), listReturn[1], listReturn[2], listReturn[3]))
    print("##############################################################################")     
    input("\n\n\n<------------------------ Press ANY KEY to CONTINUE ------------------------>")


#This is the inital frame. 
os.system ("cls") 
print(" WELCOME TO Cyrptobox. \n\n\n\n\n")
input("<------------------------ Press ANY KEY to CONTINUE ------------------------>")

#Main menu.  

option = 0
#Case option - "while" Call each function. 
while option != 4: 
    #Try is in order to halt in case there is an error in the introduced number (or during the execution).
    try:
        os.system ("cls")
        option = int(input("MAIN MENU:\n\n "\
        "##############################################################################\n\n\n"\
        "         1) SAVE NEW FILE \n\n         2) RETRIEVE SAVED FILE \n\n         3) LIST OF SAVED FILES\n\n         4) EXIT! \n\n\n"\
        "##############################################################################\n\n"\
        "Input: "))

        if option == 1: option1()
        
        elif option == 2: option2()

        elif option == 3: option3()
            
        elif option == 4: 
            os.system ("cls")    
            print("\n\n(Cyrptobox) - ByeBye")
      
        else: 
            Input("Please select one of the corresponding options.")  

    #Error --> Loops again (ex: was expected an INT and introduced a STRING.)
    except:
      os.system ("cls")
      input(" Error occurred, lets start again")

