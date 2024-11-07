/*
Write a smart contract on a test network, for Bank account of a customer for following 
operations: 
 Deposit money  
 Withdraw Money 
 Show balance 
*/


// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

contract Bank{

    uint256 balance = 0;
    address public accOwner;

    constructor()
    {
        accOwner = msg.sender;
    }

    // deposit

    function deposit() public  payable{
        require(accOwner == msg.sender,"You are not an account owner");
        require(msg.value > 0 ,"Amount should be greater than 0");
        balance += msg.value;
    }

    // withdraw
    function withdraw() public payable 
    {
        require(accOwner == msg.sender,"You are not an account owner");
        require(msg.value > 0 ,"Withdrawal money should be greater than 0");
        balance -= msg.value;
    }

    // showbalance
    function showbalance() public  view  returns (uint256)
    {
        require(accOwner == msg.sender,"You are not an account owner");
        return  balance;
    }
}