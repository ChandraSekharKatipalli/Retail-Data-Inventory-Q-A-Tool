few_shots = [
    # Example 1
    {'Question': "How many t-shirts do we have left for Nike in XS size and white color?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS';",
     'SQLResult': "Result of the SQL query",
     'Answer': "91"},

    # Example 2
    {'Question': "How much is the total price of the inventory for all L size t-shirts?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) AS total_price FROM t_shirts WHERE size = 'L';",
     'SQLResult': "Result of the SQL query",
     'Answer': "30000"},

    # Example 3
    {'Question': "What is the total number of t-shirts in stock across all brands?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts;",
     'SQLResult': "Result of the SQL query",
     'Answer': "5000"},

    # Example 4
    {'Question': "How many red color t-shirts do we have in M size?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE color = 'Red' AND size = 'M';",
     'SQLResult': "Result of the SQL query",
     'Answer': "150"},

    # Example 5
    {'Question': "Which brand has the most t-shirts in stock?",
     'SQLQuery': "SELECT brand, SUM(stock_quantity) AS total_stock FROM t_shirts GROUP BY brand ORDER BY total_stock DESC LIMIT 1;",
     'SQLResult': "Result of the SQL query",
     'Answer': "Adidas"},

    # Example 6
    {'Question': "What is the total inventory value for all t-shirts without discounts?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts;",
     'SQLResult': "Result of the SQL query",
     'Answer': "100000"},

    # Example 7
    {'Question': "How many black t-shirts are available in all sizes?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE color = 'Black';",
     'SQLResult': "Result of the SQL query",
     'Answer': "700"},

    # Example 8
    {'Question': "List all available colors for Levi's t-shirts.",
     'SQLQuery': "SELECT DISTINCT color FROM t_shirts WHERE brand = 'Levi';",
     'SQLResult': "Result of the SQL query",
     'Answer': "White, Black, Blue, Red"},

    # Example 9
    {'Question': "How many XL size t-shirts do we have for Adidas?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Adidas' AND size = 'XL';",
     'SQLResult': "Result of the SQL query",
     'Answer': "180"},

    # Example 10
    {'Question': "What is the highest priced t-shirt in stock?",
     'SQLQuery': "SELECT brand, color, size, MAX(price) FROM t_shirts;",
     'SQLResult': "Result of the SQL query",
     'Answer': "Under Armour, Black, L, $150"},

    # Example 11
    {'Question': "How many discounted t-shirts do we have in stock?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE t_shirt_id IN (SELECT t_shirt_id FROM discounts);",
     'SQLResult': "Result of the SQL query",
     'Answer': "1200"},

    # Example 12
    {'Question': "How much would we earn if all t-shirts in M size are sold at full price?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE size = 'M';",
     'SQLResult': "Result of the SQL query",
     'Answer': "30000"},

    # Example 13
    {'Question': "What is the total stock of Nike t-shirts in all colors?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike';",
     'SQLResult': "Result of the SQL query",
     'Answer': "800"},

    # Example 14
    {'Question': "How many t-shirts are in stock for each brand?",
     'SQLQuery': "SELECT brand, SUM(stock_quantity) FROM t_shirts GROUP BY brand;",
     'SQLResult': "Result of the SQL query",
     'Answer': "Nike: 800, Levi's: 1000, Adidas: 700, Puma: 500"},

    # Example 15
    {'Question': "How many white color t-shirts do we have?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE color = 'White';",
     'SQLResult': "Result of the SQL query",
     'Answer': "600"},

    # Example 16
    {'Question': "What is the average price of all t-shirts in stock?",
     'SQLQuery': "SELECT AVG(price) FROM t_shirts;",
     'SQLResult': "Result of the SQL query",
     'Answer': "$45"},

    # Example 17
    {'Question': "How many L size t-shirts are available in Puma brand?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Puma' AND size = 'L';",
     'SQLResult': "Result of the SQL query",
     'Answer': "200"},

    # Example 18
    {'Question': "What is the total number of Adidas t-shirts available?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Adidas';",
     'SQLResult': "Result of the SQL query",
     'Answer': "700"},

    # Example 19
    {'Question': "How many colors are available for Under Armour t-shirts?",
     'SQLQuery': "SELECT COUNT(DISTINCT color) FROM t_shirts WHERE brand = 'Under Armour';",
     'SQLResult': "Result of the SQL query",
     'Answer': "4"},

    # Example 20
    {'Question': "What is the minimum price of t-shirts in stock?",
     'SQLQuery': "SELECT MIN(price) FROM t_shirts;",
     'SQLResult': "Result of the SQL query",
     'Answer': "$15"},

    # Example 21
    {'Question': "How many t-shirts do we have in XL size across all brands?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE size = 'XL';",
     'SQLResult': "Result of the SQL query",
     'Answer': "1200"},

    # Example 22
    {'Question': "List the brands of t-shirts that have stock less than 100 units.",
     'SQLQuery': "SELECT DISTINCT brand FROM t_shirts WHERE stock_quantity < 100;",
     'SQLResult': "Result of the SQL query",
     'Answer': "Puma, Reebok"},

    # Example 23
    {'Question': "How much revenue will be generated if we sell all t-shirts at full price?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts;",
     'SQLResult': "Result of the SQL query",
     'Answer': "$150000"},

    # Example 24
    {'Question': "How many blue t-shirts are in stock?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE color = 'Blue';",
     'SQLResult': "Result of the SQL query",
     'Answer': "400"},

    # Example 25
    {'Question': "What is the total stock of t-shirts for each size?",
     'SQLQuery': "SELECT size, SUM(stock_quantity) FROM t_shirts GROUP BY size;",
     'SQLResult': "Result of the SQL query",
     'Answer': "XS: 500, S: 600, M: 700, L: 800, XL: 900"},

    # Example 26
    {'Question': "What are the current stock levels?",
     'SQLQuery': "SELECT brand, color, size, stock_quantity FROM t_shirts ORDER BY brand, color, size;",
     'SQLResult': "Result of the SQL query",
     'Answer': "Nike White XS: 20, Nike White S: 35, Levi's Blue M: 45, Puma Black L: 30, Adidas Red XL: 50, Van Heusen Red XS: 27, Van Heusen Red S: 50, Van Heusen Red M: 82, Van Heusen Red L: 29, Van Heusen Red XL: 83, Under Armour Gray S: 18"}
]

