"""Wallet module for key management and operations."""

from solders.keypair import Keypair
from solders.pubkey import Pubkey


def create_keypair() -> Keypair:
    """Create a new random Solana keypair.
    
    Returns:
        A new randomly generated keypair
    """
    return Keypair()


def get_keypair_from_bytes(seed_bytes: bytes) -> Keypair:
    """Create a keypair from a byte array.
    
    Args:
        seed_bytes: The seed bytes for the keypair
        
    Returns:
        A keypair generated from the provided seed
    """
    return Keypair.from_bytes(seed_bytes)


def get_pubkey_from_string(address: str) -> Pubkey:
    """Convert a base58 encoded string to a Pubkey.
    
    Args:
        address: Base58 encoded string representation of a public key
        
    Returns:
        The public key as a Pubkey object
    """
    return Pubkey.from_string(address) 