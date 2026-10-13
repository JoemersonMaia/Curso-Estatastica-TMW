WITH tb_freq_abs AS (
    SELECT 
        descCategoriaProduto, 
        count(idTransacao) AS FreqAbs

    FROM points 
    GROUP BY descCategoriaProduto
    ),

tb_freq_abs_acum AS (
    SELECT *,
        sum(FreqAbs) OVER (ORDER BY descCategoriaProduto) AS FreqAbsCum,
        1.0 * FreqAbs / (SELECT sum(FreqAbs) FROM tb_freq_abs) AS FreqRelativa
    FROM tb_freq_abs
)

SELECT *,
    sum(FreqRelativa) OVER (ORDER BY descCategoriaProduto) AS FreqRelAcum
FROm tb_freq_abs_acum



