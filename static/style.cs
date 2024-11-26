/* Estilização da lista de itens */
.data-list {
  margin-top: 20px;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.data-list div {
  background-color: #f9f9f9;
  padding: 12px;
  margin-bottom: 10px;
  border-radius: 6px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.data-list div span {
  font-weight: bold;
  color: #2c3e50;
}

.data-list div button {
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 6px 12px;
  cursor: pointer;
  font-size: 14px;
}

.data-list div button:hover {
  background-color: #c0392b;
}

.data-list div:last-child {
  margin-bottom: 0;
}
