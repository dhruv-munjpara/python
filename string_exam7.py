name=input("enter a name:")
total_len=len(name)
half_len=total_len//2
print(half_len)
first_part=name[:half_len]
last_part=name[half_len:]
print(f"first part:{first_part} last:{last_part}")
final_str=last_part+first_part
print(f"final result:{final_str}")
