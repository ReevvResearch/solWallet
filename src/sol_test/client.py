"""Solana client module for interacting with the Solana blockchain."""

from typing import Dict, Optional, Union
from solana.rpc.api import Client
from solders.pubkey import Pubkey


class SolanaClient:
    """Client for interacting with the Solana blockchain."""
    
    def __init__(self, rpc_endpoint: str = "https://api.devnet.solana.com"):
        """Initialize a Solana client.
        
        Args:
            rpc_endpoint: The Solana RPC endpoint URL (default: devnet)
        """
        self.client = Client(rpc_endpoint)
        self.endpoint = rpc_endpoint
    
    def get_balance(self, address: str):
        """Get the balance of a Solana account.
        
        Args:
            address: The account's public key as a base58 encoded string
            
        Returns:
            Response with the account balance in lamports
        """
        # Convert string address to Pubkey
        pubkey = Pubkey.from_string(address)
        return self.client.get_balance(pubkey)
    
    def get_account_info(self, address: str):
        """Get account information.
        
        Args:
            address: The account's public key as a base58 encoded string
            
        Returns:
            Response with the account information
        """
        # Convert string address to Pubkey
        pubkey = Pubkey.from_string(address)
        return self.client.get_account_info(pubkey)
    
    def get_cluster_nodes(self):
        """Get information about the nodes participating in the cluster.
        
        Returns:
            Response with information about all the nodes participating in the cluster
        """
        return self.client.get_cluster_nodes()
    
    def is_connected(self) -> bool:
        """Check if the client is connected to the RPC node.
        
        Returns:
            True if connected, False otherwise
        """
        return self.client.is_connected() 