-- 코드를 입력하세요
SELECT CAR_ID, IF(
    (SELECT COUNT(HISTORY_ID) FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16' AND A.CAR_ID = CAR_ID),
"대여중", "대여 가능") AS AVAILABILITY FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS A GROUP BY CAR_ID ORDER BY CAR_ID DESC