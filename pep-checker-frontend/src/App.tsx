import React, { useState } from "react";
import { SearchForm } from "./components/SearchForm";
import { PepResults } from "./components/PepResults";
import { PepMatch } from "./api";
import { searchPEPs } from "./api";

export function App() {
  const [results, setResults] = useState<PepMatch[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = async (query: string) => {
    setLoading(true);
    setError("");
    setHasSearched(true);
    try {
      const data = await searchPEPs(query);
      setResults(data.matches);
    } catch (err) {
      setError("Failed to fetch results.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>PEP Checker</h1>
      <SearchForm onSearch={handleSearch} />
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
      <PepResults results={results} hasSearched={hasSearched} />
    </div>
  );
}
