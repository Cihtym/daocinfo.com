import mysql from "mysql2/promise";

export default async function handler(req, res) {

    const dbconnection = await mysql.createConnection({
        host: "localhost",
        database: "products",
        //port: 8889,
        user: "admin",
        password: "password",
        socketpath: "Applications/MAMP/tmp/mysql/mysql.sock",
    });
    try {
        const query = "SELECT productid, productname, productimage FROM products"
        const value = []
        const [data] = await dbconnection.execute(query, values);
        dbconnection.end();

        res.status(200).json({ products: data });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }

}