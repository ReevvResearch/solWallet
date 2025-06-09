"""Tests for the Solana wallet module."""

import pytest
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from sol_test.wallet import create_keypair, get_keypair_from_bytes, get_pubkey_from_string


def test_create_keypair():
    """Test that a keypair can be created."""
    keypair = create_keypair()
    assert isinstance(keypair, Keypair)
    assert len(keypair.to_bytes()) == 64  # 32 bytes secret + 32 bytes public


def test_get_keypair_from_bytes():
    """Test that a keypair can be created from bytes."""
    # Generate a random keypair
    original_keypair = Keypair()
    seed_bytes = original_keypair.to_bytes()
    
    # Recreate keypair from bytes
    recreated_keypair = get_keypair_from_bytes(seed_bytes)
    
    # Verify they match
    assert recreated_keypair.pubkey() == original_keypair.pubkey()
    assert recreated_keypair.to_bytes() == original_keypair.to_bytes()


def test_get_pubkey_from_string():
    """Test that a pubkey can be created from a string."""
    # Create a keypair and get its pubkey string
    keypair = Keypair()
    pubkey_string = str(keypair.pubkey())
    
    # Convert the string back to a Pubkey
    pubkey = get_pubkey_from_string(pubkey_string)
    
    # Verify they match
    assert isinstance(pubkey, Pubkey)
    assert str(pubkey) == pubkey_string
    assert pubkey == keypair.pubkey() 