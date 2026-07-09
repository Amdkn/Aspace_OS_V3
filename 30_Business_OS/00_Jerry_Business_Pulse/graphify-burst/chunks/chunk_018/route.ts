import { NextResponse } from "next/server";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    
    // Server-side validation
    if (!body.name || !body.email || !body.company) {
      return NextResponse.json(
        { error: "Missing required fields" },
        { status: 400 }
      );
    }

    // MOCK: Simulate branching to CRM / Nova AI
    // In production, this would call Supabase, Airtable, or Make.com webhook
    console.log("[NOVA-AGENT] Nouvel audit reçu :", body);
    
    // Simulate processing time
    await new Promise((resolve) => setTimeout(resolve, 1500));

    return NextResponse.json(
      { message: "Audit request successfully logged in OS" },
      { status: 200 }
    );
  } catch (error) {
    console.error("[NOVA-AGENT] Erreur API :", error);
    return NextResponse.json(
      { error: "Internal Server Error" },
      { status: 500 }
    );
  }
}
