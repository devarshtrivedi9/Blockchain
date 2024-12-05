import tkinter as tk
from tkinter import messagebox, scrolledtext
from blockchain import Blockchain

# Create an instance of Blockchain
blockchain = Blockchain()

class BlockchainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blockchain GUI")
        self.root.geometry("600x500")

        self.transaction_frame = tk.LabelFrame(self.root, text="Create Transaction")
        self.transaction_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(self.transaction_frame, text="From:").grid(row=0, column=0, padx=5, pady=5)
        self.from_entry = tk.Entry(self.transaction_frame, width=30)
        self.from_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.transaction_frame, text="To:").grid(row=1, column=0, padx=5, pady=5)
        self.to_entry = tk.Entry(self.transaction_frame, width=30)
        self.to_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.transaction_frame, text="Amount:").grid(row=2, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(self.transaction_frame, width=30)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(self.transaction_frame, text="Submit Transaction", command=self.create_transaction)
        self.submit_button.grid(row=3, columnspan=2, pady=10)

        self.mine_button = tk.Button(self.root, text="Mine Block", command=self.mine_block)
        self.mine_button.pack(pady=10)

        self.output_frame = tk.LabelFrame(self.root, text="Blockchain")
        self.output_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.blockchain_display = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, width=70, height=15)
        self.blockchain_display.pack()

        self.refresh_button = tk.Button(self.root, text="Refresh Blockchain", command=self.display_blockchain)
        self.refresh_button.pack(pady=10)

    def create_transaction(self):
        from_addr = self.from_entry.get()
        to_addr = self.to_entry.get()
        amount = self.amount_entry.get()

        if not from_addr or not to_addr or not amount:
            messagebox.showwarning("Input Error", "All fields must be filled!")
            return

        try:
            transaction = {"from": from_addr, "to": to_addr, "amount": int(amount)}
            blockchain.create_transaction(transaction)
            messagebox.showinfo("Transaction", "Transaction added to pending transactions.")
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number.")

    def mine_block(self):
        blockchain.mine_pending_transactions("MinerAddress")
        messagebox.showinfo("Mining", "Block successfully mined!")
        self.display_blockchain()

    def display_blockchain(self):
        self.blockchain_display.delete(1.0, tk.END)
        for block in blockchain.chain:
            self.blockchain_display.insert(tk.END, f"Index: {block.index}\n")
            self.blockchain_display.insert(tk.END, f"Previous Hash: {block.previous_hash}\n")
            self.blockchain_display.insert(tk.END, f"Timestamp: {block.timestamp}\n")
            self.blockchain_display.insert(tk.END, f"Data: {block.data}\n")
            self.blockchain_display.insert(tk.END, f"Hash: {block.hash}\n")

            self.blockchain_display.insert(tk.END, "-"*40 + "\n")

    def clear_entries(self):
        self.from_entry.delete(0, tk.END)
        self.to_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BlockchainApp(root)
    root.mainloop()
