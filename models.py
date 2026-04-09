"""
CRUD-функции для student_bot.
"""

from database.db import get_db


# ── ЗАКАЗЫ ──────────────────────────────────────────────────────────────────

async def save_order(user_id, username, full_name, work_type, topic, deadline, phone, details) -> int:
    db = await get_db()
    try:
        cur = await db.execute(
            "INSERT INTO orders (user_id, username, full_name, work_type, topic, deadline, phone, details) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, username, full_name, work_type, topic, deadline, phone, details),
        )
        await db.commit()
        return cur.lastrowid
    finally:
        await db.close()


async def get_order(order_id: int):
    db = await get_db()
    try:
        cur = await db.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
        return await cur.fetchone()
    finally:
        await db.close()


async def get_orders(status: str = None, limit: int = 15) -> list:
    db = await get_db()
    try:
        if status:
            cur = await db.execute(
                "SELECT * FROM orders WHERE status = ? ORDER BY id DESC LIMIT ?",
                (status, limit),
            )
        else:
            cur = await db.execute(
                "SELECT * FROM orders ORDER BY id DESC LIMIT ?", (limit,)
            )
        return await cur.fetchall()
    finally:
        await db.close()


async def update_order_status(order_id: int, status: str) -> None:
    db = await get_db()
    try:
        await db.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
        await db.commit()
    finally:
        await db.close()


async def get_stats() -> dict:
    db = await get_db()
    try:
        total   = (await (await db.execute("SELECT COUNT(*) FROM orders")).fetchone())[0]
        new_o   = (await (await db.execute("SELECT COUNT(*) FROM orders WHERE status='new'")).fetchone())[0]
        done    = (await (await db.execute("SELECT COUNT(*) FROM orders WHERE status='done'")).fetchone())[0]
        new_c   = (await (await db.execute("SELECT COUNT(*) FROM complaints WHERE status='new'")).fetchone())[0]
        return {"total": total, "new": new_o, "done": done, "new_complaints": new_c}
    finally:
        await db.close()


# ── ЖАЛОБЫ ──────────────────────────────────────────────────────────────────

async def save_complaint(user_id, username, full_name, text) -> int:
    db = await get_db()
    try:
        cur = await db.execute(
            "INSERT INTO complaints (user_id, username, full_name, text) VALUES (?, ?, ?, ?)",
            (user_id, username, full_name, text),
        )
        await db.commit()
        return cur.lastrowid
    finally:
        await db.close()


async def get_complaints(limit: int = 10) -> list:
    db = await get_db()
    try:
        cur = await db.execute(
            "SELECT * FROM complaints ORDER BY id DESC LIMIT ?", (limit,)
        )
        return await cur.fetchall()
    finally:
        await db.close()


async def resolve_complaint(complaint_id: int) -> None:
    db = await get_db()
    try:
        await db.execute(
            "UPDATE complaints SET status = 'resolved' WHERE id = ?", (complaint_id,)
        )
        await db.commit()
    finally:
        await db.close()
