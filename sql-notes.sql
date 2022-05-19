  /*

 BACKGROUND:
 
 The following schema is a subset of a relational database of a grocery store
 chain. This chain sells many products of different product classes to its
 customers across its different stores. It also conducts many different
 promotion campaigns.
 
 The relationship between the four tables we want to analyze is depicted below:
 
       # sales                                # products
       +------------------+---------+         +---------------------+---------+
       | product_id       | INTEGER |>--------| product_id          | INTEGER |
       | store_id         | INTEGER |    +---<| product_class_id    | INTEGER |
       | customer_id      | INTEGER |    |    | brand_name          | VARCHAR |
  +---<| promotion_id     | INTEGER |    |    | product_name        | VARCHAR |
  |    | store_sales      | DECIMAL |    |    | is_low_fat_flg      | TINYINT |
  |    | store_cost       | DECIMAL |    |    | is_recyclable_flg   | TINYINT |
  |    | units_sold       | DECIMAL |    |    | gross_weight        | DECIMAL |
  |    | transaction_date | DATE    |    |    | net_weight          | DECIMAL |
  |    +------------------+---------+    |    +---------------------+---------+
  |                                      |
  |    # promotions                      |    # product_classes
  |    +------------------+---------+    |    +---------------------+---------+
  +----| promotion_id     | INTEGER |    +----| product_class_id    | INTEGER |
       | promotion_name   | VARCHAR |         | product_subcategory | VARCHAR |
       | media_type       | VARCHAR |         | product_category    | VARCHAR |
       | cost             | DECIMAL |         | product_department  | VARCHAR |
       | start_date       | DATE    |         | product_family      | VARCHAR |
       | end_date         | DATE    |         +---------------------+---------+
       +------------------+---------+

 */ 
/*
 PROMPT:
 -- What percent of all products in the grocery chain's catalog
 -- are both low fat and recyclable?
 

 EXPECTED OUTPUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +----------------------------+
 | pct_low_fat_and_recyclable |
 +----------------------------+
 |        15.3846153846153846 |
 +----------------------------+

HINTS
- How do we get products that are both low fat and recyclable?
- How do we convert the result into a percentage?
Spoiler: We can use Avg and CASE.

 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ---------------- 
 */

/*
SELECT 100.0 * (
SELECT COUNT(*) FROM products
WHERE is_low_fat_flg and is_recyclable_flg
)/COUNT(*)  AS pct_low_fat_and_recyclable
FROM products
*/

SELECT 100 * AVG(CASE WHEN is_low_fat_flg and is_recyclable_flg THEN 1.0 ELSE 0 END) AS pct_low_fat_and_recyclable
FROM products

/*
 PROMPT:
 -- What are the top five (ranked in decreasing order)
 -- single-channel media types that correspond to the most money
 -- the grocery chain had spent on its promotional campaigns?

 Single Media Channel Types are promotions that contain only one media type.

 EXPECTED OUPTUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +---------------------------+------------+
 | single_channel_media_type | total_cost |
 +---------------------------+------------+
 | In-Store Coupon           | 70800.0000 |
 | Street Handout            | 70627.0000 |
 | Radio                     | 60192.0000 |
 | Sunday Paper              | 56994.0000 |
 | Product Attachment        | 50815.0000 |
 +---------------------------+------------+
 
HINTS
- How do we find all promotions that contain only one media type?
Spoiler: We can use LIKE clause.

-------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 */

SELECT media_type AS single_channel_media_type, SUM(cost) AS total_cost, ROW_NUMBER() OVER ()
FROM promotions
WHERE media_type NOT LIKE "%,%"
GROUP BY media_type
ORDER BY SUM(cost) DESC
LIMIT 5

/*
 PROMPT:
 -- Of sales that had a valid promotion, the VP of marketing
 -- wants to know what % of transactions occur on either
 -- the very first day or the very last day of a promotion campaign.
 
 
 EXPECTED OUTPUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +-------------------------------------------------------------+
 | pct_of_transactions_on_first_or_last_day_of_valid_promotion |
 +-------------------------------------------------------------+
 |                                         41.9047619047619048 |
 +-------------------------------------------------------------+
  
HINTS
- How do we find all sales between the start and end date?
- How do we find sales with valid promotions?
You can join both the sales and promotions tables based on the promotion_id.

 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 */

SELECT 100.0 * AVG(CASE WHEN (s.transaction_date = p.start_date OR s.transaction_date = p.end_date) THEN 1.0 ELSE 0 END)
AS pct_of_transactions_on_first_or_last_day_of_valid_promotion
FROM sales s
JOIN promotions p
USING (promotion_id)

/*
 PROMPT
 -- The CMO is interested in understanding how the sales of different
 -- product families are affected by promotional campaigns.
 -- To do so, for each of the available product families,
 -- show the total number of units sold,
 -- as well as the ratio of units sold that had a valid promotion
 -- to units sold without a promotion,
 -- ordered by increasing order of total units sold.
 
 
 EXPECTED OUTPUT
 Note: Please use the column name(s) specified in the expected output in your solution.
 +----------------+------------------+--------------------------------------------------+
 | product_family | total_units_sold | ratio_units_sold_with_promo_to_sold_without_promo|
 +----------------+------------------+--------------------------------------------------+
 | Drink          |          43.0000 |                           0.79166666666666666667 |
 | Non-Consumable |         176.0000 |                           0.76000000000000000000 |
 | Food           |         564.0000 |                           0.75155279503105590062 |
 +----------------+------------------+--------------------------------------------------+
 
 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 */

SELECT pc.product_family, SUM(s.units_sold) AS total_units_sold,
1.0*SUM(s.units_sold * (CASE WHEN s.promotion_id is 0 THEN 0 ELSE 1 END)) / SUM(s.units_sold * (CASE WHEN s.promotion_id is 0 THEN 1 ELSE 0 END)) AS ratio_units_sold_with_promo_to_sold_without_promo
FROM product_classes pc
LEFT JOIN products p
USING (product_class_id)
LEFT JOIN sales s
USING (product_id)
GROUP BY pc.product_family
ORDER BY total_units_sold ASC

/*
 PROMPT:
 -- The VP of Sales feels that some product categories don't sell
 -- and can be completely removed from the inventory.
 -- As a first pass analysis, they want you to find what percentage
 -- of product categories have never been sold.
 
 EXPECTED OUTPUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +-----------------------------------+
 | pct_product_categories_never_sold |
 +-----------------------------------+
 |               13.8888888888888889 |
 +-----------------------------------+

 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 */

SELECT 100.0 - 100.0 * (SELECT COUNT(DISTINCT product_category)
FROM product_classes pc
JOIN products
USING (product_class_id)
JOIN sales
USING (product_id))/ COUNT(DISTINCT product_category) AS pct_product_categories_never_sold
FROM product_classes pc



