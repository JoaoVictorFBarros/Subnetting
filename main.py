import ipaddress

def calcular_subredes(ip_rede, num_subredes):
    try:

        rede = ipaddress.ip_network(ip_rede, strict=False)

        novo_prefixo = rede.prefixlen + (num_subredes - 1).bit_length()
        subredes = list(rede.subnets(new_prefix=novo_prefixo))
        subredes = subredes[:num_subredes]

        print(f"Rede original: {rede}")
        print(f"Nova máscara para {num_subredes} sub-redes: /{novo_prefixo}")
        print("-" * 40)

        for i, subrede in enumerate(subredes, 1):
            print(f"Sub-rede {i}:")
            print(f"Endereço de rede: {subrede.network_address}")
            print(f"Primeiro IP: {list(subrede.hosts())[0]}")
            print(f"Último IP: {list(subrede.hosts())[-1]}")
            print(f"Endereço de broadcast: {subrede.broadcast_address}")
            print("-" * 40)

    except ValueError as e:
        print(f"Erro: {e}")

ip_rede = input("Digite o endereço de rede (ex: 192.168.0.0/24): ")
num_subredes = int(input("Digite o número de sub-redes desejadas: "))

calcular_subredes(ip_rede, num_subredes)
