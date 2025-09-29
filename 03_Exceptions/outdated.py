months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#Solution I wrote
# def main():
#     while True:
#         user_date = str(input("Date: ")).title()
#         if "/" in user_date:
#             month, day, year = user_date.split("/")
            
#             if int(day) <= 31:
#                 print(f"{year}-{int(month):02}-{int(day):02}")
#                 break


#         elif any(month in user_date for month in months):
#             user_date = user_date.replace(",", "")
#             month, day, year = user_date.split(" ")
#             month = months.index(month) + 1
#             if int(day) <= 31:
#                 print(f"{year}-{int(month):02}-{int(day):02}")
#                 break

#Solution that Chatgpt wrote
def main():
    while True:
        date_strip = input("Date: ").strip()

        try:
            if "/" in date_strip:
                month, day, year = date_strip.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            else:
                parts = date_strip.replace(",", "").strip()
                month = months.index(parts[0]) + 1
                day = int(parts[1])
                year = int(parts[2])

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except:
            continue


if __name__ == "__main__":
    main()