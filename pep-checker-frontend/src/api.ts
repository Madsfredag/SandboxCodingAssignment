export interface PepMatch {
    name: string;
    score: number;
    _links: { self: { href: string } };
  }
  
  export interface PepMatchResponse {
    _links: { self: { href: string } };
    matches: PepMatch[];
  }
  
  export async function searchPEPs(query: string): Promise<PepMatchResponse> {
    const response = await fetch(`http://localhost:8000/pep/search?name=${query}`);
    if (!response.ok) throw new Error("Failed to fetch results");
    return await response.json();
  }