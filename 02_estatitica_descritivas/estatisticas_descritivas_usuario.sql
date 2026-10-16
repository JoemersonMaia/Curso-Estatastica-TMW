WITH tb_usuario AS(
    SELECT 
        idUsuario,
        sum(qtdPontos) AS QtdPontos
    FROM points
    GROUP BY idUsuario
),

tb_subset_mediana AS (
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count (*) % 2 == 0 FROM tb_usuario)
    OFFSET (SELECT 2 * count (*) / 4 from tb_usuario)

),

tb_mediana AS (
SELECT AVG(qtdPontos) AS Mediana
FROM tb_subset_mediana

),

tb_subset_quartil_1 AS (
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count (*) % 2 == 0 FROM tb_usuario)
    OFFSET (SELECT 1 * count (*) / 4 from tb_usuario)

),

tb_quartil_01 AS (
    SELECT avg(qtdPontos) AS quartil_01
    FROM tb_subset_quartil_1
),

tb_subset_quartil_3 AS (
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count (*) % 2 == 0 FROM tb_usuario)
    OFFSET (SELECT 3 * count (*) / 4 from tb_usuario)

),

tb_quartil_03 AS (
    SELECT avg(qtdPontos) AS quartil_03
    FROM tb_subset_quartil_3
),

tb_stats AS(
    SELECT min(qtdPontos) AS minimo,
        avg(qtdPontos) AS media,
        max(qtdPontos) AS maximo

   FROM tb_usuario
   
)

SELECT * FROM tb_mediana, tb_quartil_01, tb_quartil_03, tb_stats