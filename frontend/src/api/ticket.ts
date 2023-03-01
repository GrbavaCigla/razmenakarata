export async function create_ticket(
  event_id: number,
  package_name: string,
  online: boolean,
  price: number,
  token: string,
) {
  const resp = await fetch(`http://127.0.0.1:8000/api/v1/events/${event_id}/tickets/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify({
        "package": package_name,
        "online": online,
        "price": price,
        // TODO: Remove hardcoded value
        "amount": 1, 
    }),
  });
}
