export class NonRepeatingPicker {
  constructor(items = []) {
    this.original = [...items];
    this.pool = [];
    this.index = 0;
    this.#refill();
  }

  next() {
    if (!this.original.length) {
      return null;
    }

    if (this.index >= this.pool.length) {
      this.#refill();
    }

    const item = this.pool[this.index];
    this.index += 1;
    return item;
  }

  #refill() {
    this.pool = [...this.original];
    for (let i = this.pool.length - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.pool[i], this.pool[j]] = [this.pool[j], this.pool[i]];
    }
    this.index = 0;
  }
}
