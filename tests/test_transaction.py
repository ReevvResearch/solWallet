"""Tests for the Solana transaction module."""

import pytest
from unittest.mock import MagicMock, patch
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from sol_test.transaction import create_transfer_transaction, send_transaction


def test_create_transfer_transaction():
    """Test that a transfer transaction can be created."""
    # Create test keypairs
    from_keypair = Keypair()
    to_pubkey = Keypair().pubkey()
    lamports = 1000
    # Use a valid blockhash format
    recent_blockhash = "4uQeVj5tqViQh7yWWGStvkEG1Zmhx6uasJtWCJziofM"
    
    # Create transaction
    tx = create_transfer_transaction(
        from_keypair=from_keypair,
        to_pubkey=to_pubkey, 
        lamports=lamports,
        recent_blockhash=recent_blockhash
    )
    
    # Basic assertions about the mock transaction
    assert hasattr(tx, 'signatures')
    assert hasattr(tx, 'message')
    assert len(tx.signatures) > 0


def test_send_transaction_with_attribute():
    """Test that a transaction can be sent with attribute-style response."""
    # Mock the client and transaction
    mock_client = MagicMock()
    mock_transaction = MagicMock()
    
    # Set up the mock response with attribute access
    expected_signature = "5UvMA4fRS852ZLFQ8j62DMZeHiyGE6JKNHu9sNQqK2W6juE88ERRq9zXhNvFZNGUvhQcij9Rh5kC9saYyjqJkEVa"
    mock_response = MagicMock()
    mock_response.value = expected_signature
    mock_client.send_transaction.return_value = mock_response
    
    # Call the function
    result = send_transaction(mock_client, mock_transaction)
    
    # Assertions
    assert mock_client.send_transaction.called
    assert mock_client.send_transaction.call_count == 1
    assert mock_client.send_transaction.call_args[0][0] == mock_transaction
    assert result == expected_signature


def test_send_transaction_with_dict():
    """Test that a transaction can be sent with dict-style response."""
    # Mock the client and transaction
    mock_client = MagicMock()
    mock_transaction = MagicMock()
    
    # Set up the mock response with dict access
    expected_signature = "5UvMA4fRS852ZLFQ8j62DMZeHiyGE6JKNHu9sNQqK2W6juE88ERRq9zXhNvFZNGUvhQcij9Rh5kC9saYyjqJkEVa"
    mock_response = {'result': expected_signature}
    mock_client.send_transaction.return_value = mock_response
    
    # Call the function
    result = send_transaction(mock_client, mock_transaction)
    
    # Assertions
    assert mock_client.send_transaction.called
    assert mock_client.send_transaction.call_count == 1
    assert mock_client.send_transaction.call_args[0][0] == mock_transaction
    assert result == expected_signature 