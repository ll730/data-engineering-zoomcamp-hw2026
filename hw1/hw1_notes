# Module 1 Homework: Docker & SQL

---

## Question 1: Understanding Docker images

**Task:** Run docker with `python:3.13` image and check pip version.

```bash
docker run -it --entrypoint=bash python:3.13
pip --version
```

**Answer:** `25.3`

---

## Question 2: Understanding Docker networking

**Task:** What hostname and port should pgAdmin use to connect to postgres?

**Key concept:** pgAdmin runs inside Docker, so it uses:
- Service name (`db`) as hostname
- Internal port (`5432`)

**Answer:** `db:5432`

---

## Question 3: Counting short trips

**Task:** Count trips in November 2025 with trip_distance <= 1 mile.

```sql
SELECT COUNT(*)
FROM green_taxi_trips t
WHERE t."lpep_pickup_datetime" >= '2025-11-01'
  AND t."lpep_pickup_datetime" < '2025-12-01'
  AND t."trip_distance" <= 1.0;
```

**Note:** Using `>=` and `<` (not BETWEEN) because upper bound is exclusive.

**Answer:** `8007`

---

## Question 4: Longest trip for each day

**Task:** Which pickup day had the longest trip distance? (exclude trips >= 100 miles)

```sql
SELECT t."lpep_pickup_datetime", t."trip_distance"
FROM green_taxi_trips t
WHERE t."trip_distance" < 100
ORDER BY t."trip_distance" DESC
LIMIT 1;
```

**Answer:** `2025-11-14`

---

## Question 5: Biggest pickup zone

**Task:** Which pickup zone had the largest total_amount (sum) on November 18th, 2025?

```sql
SELECT z."Zone", SUM(t.total_amount) AS total_amount
FROM green_taxi_trips t
JOIN zones z
  ON t."PULocationID" = z."LocationID"
WHERE t."lpep_pickup_datetime" >= '2025-11-18'
  AND t."lpep_pickup_datetime" < '2025-11-19'
GROUP BY z."Zone"
ORDER BY 2 DESC;
```

**Note:** Using `SUM()` not `COUNT()` - question asks for sum of total_amount.

**Answer:** `East Harlem North`

---

## Question 6: Largest tip

**Task:** For pickups in "East Harlem North" in November 2025, which dropoff zone had the largest tip?

```sql
SELECT z2."Zone", t."tip_amount"
FROM green_taxi_trips t
JOIN zones z1
  ON t."PULocationID" = z1."LocationID"
JOIN zones z2
  ON t."DOLocationID" = z2."LocationID"
WHERE z1."Zone" = 'East Harlem North'
  AND t."lpep_pickup_datetime" >= '2025-11-01'
  AND t."lpep_pickup_datetime" < '2025-12-01'
ORDER BY 2 DESC;
```

**Note:** Double JOIN - `z1` for pickup zone (filter), `z2` for dropoff zone (result).

**Answer:** `Yorkville West`

---

## Question 7: Terraform Workflow

**Task:** Which sequence describes the workflow for:
1. Downloading the provider plugins and setting up backend
2. Generating proposed changes and auto-executing the plan
3. Remove all resources managed by terraform

**Answer:** `terraform init, terraform apply -auto-approve, terraform destroy`