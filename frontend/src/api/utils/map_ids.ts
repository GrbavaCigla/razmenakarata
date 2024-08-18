export async function map_ids<T>(ids: number[], func: (id: number) => Promise<T | null>) {
    let unique_ids = [...new Set(ids)];

    let promises = unique_ids.map((id) => func(id));

    let data = await Promise.all(promises);

    let object: { [id: number] : T; } = {};

    for(let [index, id] of unique_ids.entries()) {
        if (data[index] != null) {
            object[id] = data[index];
        }
    }

    return object;
}