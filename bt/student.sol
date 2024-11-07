/*
Write a program in solidity to create Student data. Use the following constructs: 
 Structures 
 Arrays 
 Fallback 
Deploy this as smart contract on Ethereum and Observe the transaction fee and Gas values.
*/


// SPDX-License-Identifier: GPL-3.0

pragma  solidity ^0.8.0;

contract Studentdata{

    // structure
    struct Student{
        string name;
        uint256 rollno;
    }
    // array

    Student []public  studentarr;

    function addStudent(string memory name , uint rollno) public
    {
        for(uint i = 0; i < studentarr.length; i++)
        {
            if(studentarr[i].rollno == rollno)
            {
                revert("Student with this rollno already exists");
            }
        }
        studentarr.push(Student(name,rollno));
    }

    function getStudentsLength() public view returns (uint)
    {
        return  studentarr.length;
    }

    function displayAllStudent() public view  returns (Student[] memory)
    {
        return  studentarr;
    }

    function getStudentByIndex(uint idx) public view  returns (Student memory)
    {
        require(idx < studentarr.length , "index out of bound");
        return studentarr[idx];
    }

    // fallback

    fallback() external payable {
        // this function will handle external function calls that is not there in our contract
     }

     receive() external payable { 
        // this function will handle the ether sent by external user but without data mention
     }

}