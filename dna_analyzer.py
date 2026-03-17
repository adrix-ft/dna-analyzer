from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio.Blast import NCBIWWW, NCBIXML


def validate_dna_sequence(sequence):
    """Checks if the sequence is a valid DNA string."""
    valid_bases = set('ATCGNatcgn')
    return all(base in valid_bases for base in sequence)


def print_section_title(title):
    """Prints a formatted section title."""
    print(f"\n{'='*50}")
    print(f"{title.upper()}")
    print(f"{'='*50}")


def blast_ncbi(dna_sequence):
    """Searches NCBI BLAST and returns organism details."""
    print("\n🔍 Searching NCBI BLAST (this may take a few seconds)...")

    try:
        result_handle = NCBIWWW.qblast(
            program="blastn",
            database="nt",
            sequence=dna_sequence,
            hitlist_size=1
        )

        blast_record = NCBIXML.read(result_handle)

        if blast_record.alignments:
            alignment = blast_record.alignments[0]
            hsp = alignment.hsps[0]

            print_section_title("ncbi blast result")
            print(f"🦠 Description / Organism:")
            print(f"   {alignment.title}")
            print(f"\n📎 Accession ID: {alignment.accession}")
            print(f"📊 Alignment length: {hsp.align_length}")
            print(f"📈 E-value: {hsp.expect}")

        else:
            print("❌ No significant match found on NCBI.")

    except Exception as e:
        print("⚠️ Unable to access NCBI at the moment.")
        print("Reason:", e)


def dna_analyzer():
    print("=== 🧬 DNA SEQUENCE ANALYZER TOOL ===")
    print("Enter/Paste your DNA sequence (type 'exit' to quit)")
    print("-" * 50)

    while True:
        user_input = input("\nDNA Sequence: ").upper().strip()

        if user_input.lower() == 'exit':
            print("Exiting analyzer. Goodbye!")
            break

        if user_input == "":
            continue

        # Clean the input
        dna_seq = ''.join([char for char in user_input if char in 'ATCGN'])

        if not validate_dna_sequence(dna_seq):
            print("❌ ERROR: Invalid characters detected. Use only A, T, C, G, or N.")
            continue

        seq_obj = Seq(dna_seq)
        seq_length = len(seq_obj)

        print_section_title("input summary")
        print(f"🔢 Length: {seq_length} base pairs")
        if 'N' in dna_seq:
            print(f"⚠️  Contains {dna_seq.count('N')} undefined base(s) (N)")

        # Translation trimming
        remainder = seq_length % 3
        if remainder != 0:
            print(f"⚠️  Length not divisible by 3. Trimming {remainder} base(s) for translation.")
            seq_obj_trimmed = seq_obj[:-remainder]
        else:
            seq_obj_trimmed = seq_obj

        print_section_title("nucleotide composition")
        print(f"A: {seq_obj.count('A'):>6} ({seq_obj.count('A')/seq_length*100:>5.1f}%)")
        print(f"T: {seq_obj.count('T'):>6} ({seq_obj.count('T')/seq_length*100:>5.1f}%)")
        print(f"C: {seq_obj.count('C'):>6} ({seq_obj.count('C')/seq_length*100:>5.1f}%)")
        print(f"G: {seq_obj.count('G'):>6} ({seq_obj.count('G')/seq_length*100:>5.1f}%)")
        if seq_obj.count('N') > 0:
            print(f"N: {seq_obj.count('N'):>6} ({seq_obj.count('N')/seq_length*100:>5.1f}%)")

        gc_content = gc_fraction(seq_obj) * 100
        print(f"\n🧮 GC Content: {gc_content:.2f}%")

        print_section_title("sequence transformations")
        print("🔄 Reverse Complement:")
        print(f"   {seq_obj.reverse_complement()}")

        print("\n🔁 Transcription (to RNA):")
        print(f"   {seq_obj.transcribe()}")

        print_section_title("protein translation")
        if remainder != 0:
            print(f"📏 Using trimmed sequence ({len(seq_obj_trimmed)} bp) for translation:")

        protein_seq = seq_obj_trimmed.translate()
        print(f"🧪 Amino Acid Sequence ({len(protein_seq)} residues):")
        print(f"   {protein_seq}")

        print("\n📋 Formatted Protein Sequence:")
        for i in range(0, len(protein_seq), 50):
            print(f"   {protein_seq[i:i+50]}")

        # Ask user if they want NCBI BLAST
        choice = input("\nDo you want to search this sequence on NCBI? (y/n): ").lower()
        if choice == 'y':
            blast_ncbi(dna_seq)

        print_section_title("analysis complete")
        print("Ready for next sequence...\n")


# Run the analyzer
if __name__ == "__main__":
    dna_analyzer()
