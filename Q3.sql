SELECT article.article_id FROM article
LEFT JOIN category_article_mapping ON article.article_id = category_article_mapping.category_id
AS category_match;

SELECT COUNT(DISTINCT category_match )FROM article AS category_count;

SELECT category_count FROM article 
ORDER BY category_count DESC;

SELECT order_id, owner_name FROM 'owner'