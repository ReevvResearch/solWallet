#!/usr/bin/env python3
"""Example script demonstrating Solana interactions."""

from sol_test.client import SolanaClient
from sol_test.wallet import create_keypair
from solders.pubkey import Pubkey

def main():
    """Run example operations."""
    # Initialize client
    client = SolanaClient()
    
    # Check connection
    is_connected = client.is_connected()
    print(f"Connected to Solana network: {is_connected}")
    
    # Create a new keypair
    keypair = create_keypair()
    print(f"Generated new keypair:")
    print(f"  Public key: {keypair.pubkey()}")
    print(f"  Private key (first 4 bytes): {keypair.to_bytes()[:4].hex()}")
    
    # Get balance of a known account
    # Solana Foundation address
    address = "4beBxnHZxJWRDUQCFVmK5adKQHvMypB7e2e6xPQghQtY"
    balance_response = client.get_balance(address)
    
    # Handle different response structures in recent solana-py versions
    if hasattr(balance_response, 'result') and hasattr(balance_response.result, 'value'):
        balance_lamports = balance_response.result.value
    else:
        # Handle newer response format
        balance_lamports = balance_response.value
    
    balance_sol = balance_lamports / 1_000_000_000  # 1 SOL = 10^9 lamports
    print(f"\nBalance of {address}:")
    print(f"  {balance_lamports} lamports")
    print(f"  {balance_sol:.9f} SOL")
    
    # Get cluster information
    print("\nCluster nodes:")
    nodes_response = client.get_cluster_nodes()
    
    # Handle the cluster nodes response which might have different formats
    try:
        # Try to iterate the response directly
        for i, node in enumerate(nodes_response, 1):
            if i > 3:
                print(f"  ... and {len(nodes_response) - 3} more nodes")
                break
                
            if isinstance(node, dict):
                print(f"  {i}. {node['pubkey']} - version: {node.get('version', 'unknown')}")
            else:
                # Handle newer response format where node might be an object
                pubkey = getattr(node, "pubkey", "unknown")
                version = getattr(node, "version", "unknown")
                print(f"  {i}. {pubkey} - version: {version}")
    except TypeError:
        # If the response is not directly iterable, try to get the result attribute
        if hasattr(nodes_response, 'value'):
            nodes = nodes_response.value
        elif hasattr(nodes_response, 'result'):
            nodes = nodes_response.result
        else:
            print("  Unable to parse cluster nodes response")
            return
            
        # Try to show the first 3 nodes
        total_nodes = getattr(nodes, '__len__', lambda: 0)()
        shown_nodes = min(3, total_nodes)
        
        for i in range(shown_nodes):
            try:
                node = nodes[i]
                if isinstance(node, dict):
                    print(f"  {i+1}. {node.get('pubkey', 'unknown')} - version: {node.get('version', 'unknown')}")
                else:
                    print(f"  {i+1}. {getattr(node, 'pubkey', 'unknown')} - version: {getattr(node, 'version', 'unknown')}")
            except (IndexError, TypeError):
                print(f"  {i+1}. Unable to parse node information")
        
        if total_nodes > 3:
            print(f"  ... and {total_nodes - 3} more nodes")

if __name__ == "__main__":
    main() 