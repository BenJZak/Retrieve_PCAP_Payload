from scapy.all import rdpcap

def decode_pcap(file_path):
    try:
        #read packets from the PCAP file
        packets = rdpcap(file_path)

        #extract and decode payload data from each packet
        for packet in packets:
            if packet.haslayer("Raw"):
                payload = packet.getlayer("Raw").load
                decoded_data = payload.decode("utf-8", errors="ignore")
                print(f"Decoded Data: {decoded_data}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    #specify the path to *YOUR* PCAP file, nothing else should be mofified
    pcap_file_path = "/Users/benzakielarz/Downloads/TreasureMap1.pcap"
    #call the function to decode and print payload data
    decode_pcap(pcap_file_path)