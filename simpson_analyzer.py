import pandas as pd
from typing import Dict

class SimpsonAnalyzer:
    """Tool to analyze Simpson's Paradox in clinical data"""
    
    def __init__(self):
        self.data = pd.DataFrame()
        self.group_col = ''
        self.treatment_col = ''
        self.outcome_col = ''
    
    def input_data(self):
        """Interactive data input"""
        print("\n=== Simpson's Paradox Analyzer ===")
        self.group_col = input("Group variable (e.g., 'size'): ")
        self.treatment_col = input("Treatment variable (e.g., 'tx'): ")
        self.outcome_col = input("Outcome variable (e.g., 'success'): ")
        
        groups = input(f"{self.group_col} values (comma sep): ").split(',')
        groups = [g.strip() for g in groups]
        treatments = input(f"{self.treatment_col} types (comma sep): ").split(',')
        treatments = [t.strip() for t in treatments]
        
        records = []
        print("\nEnter counts for each combination:")
        for group in groups:
            for tx in treatments:
                print(f"\n{group} + {tx}:")
                total = int(input("  Total cases: "))
                successes = int(input("  Successes: "))
                records.append({
                    self.group_col: group,
                    self.treatment_col: tx,
                    'total': total,
                    'successes': successes,
                    'failures': total - successes
                })
        
        expanded = []
        for r in records:
            expanded.extend([{
                self.group_col: r[self.group_col],
                self.treatment_col: r[self.treatment_col],
                self.outcome_col: 1} for _ in range(r['successes'])])
            expanded.extend([{
                self.group_col: r[self.group_col],
                self.treatment_col: r[self.treatment_col],
                self.outcome_col: 0} for _ in range(r['failures'])])
        
        self.data = pd.DataFrame(expanded)
        print("\nData entered successfully!")
    
    def analyze(self):
        """Run full analysis"""
        if self.data.empty:
            print("No data to analyze!")
            return
        
        rates = self._calc_rates()
        props = self._calc_props()
        cond_met = self._check_condition(props)
        
        print("\n=== Results ===")
        print("\nSuccess Rates (%):")
        for tx, tx_data in rates.items():
            print(f"\n{tx}:")
            for grp, rate in tx_data.items():
                if grp != 'overall':
                    print(f"  {grp}: {rate:.1f}%")
            print(f"  Overall: {tx_data['overall']:.1f}%")
        
        print("\nSubgroup Proportions:")
        for tx, prop in props.items():
            print(f"  {tx}: {prop:.2f}")
        
        print("\nCondition met?", "✓ YES" if cond_met else "✗ NO")
        if not cond_met:
            self._check_paradox(rates)
    
    def _calc_props(self) -> Dict[str, float]:
        """Calculate subgroup proportions"""
        props = {}
        for tx in self.data[self.treatment_col].unique():
            tx_data = self.data[self.data[self.treatment_col] == tx]
            counts = tx_data[self.group_col].value_counts().sort_index()
            if len(counts) >= 2:
                props[tx] = counts.iloc[0]/counts.iloc[1]
        return props
    
    def _calc_rates(self) -> Dict[str, Dict[str, float]]:
        """Calculate success rates"""
        rates = {}
        for tx in self.data[self.treatment_col].unique():
            tx_data = self.data[self.data[self.treatment_col] == tx]
            rates[tx] = {}
            for grp in self.data[self.group_col].unique():
                grp_data = tx_data[tx_data[self.group_col] == grp]
                total = len(grp_data)
                rates[tx][grp] = (grp_data[self.outcome_col].sum()/total)*100 if total else 0.0
            rates[tx]['overall'] = (tx_data[self.outcome_col].sum()/len(tx_data))*100
        return rates
    
    def _check_condition(self, props: Dict[str, float], thresh=0.1) -> bool:
        """Check similarity condition"""
        if len(props) < 2: return True
        vals = list(props.values())
        return all(abs(v-vals[0])/vals[0] <= thresh for v in vals[1:])
    
    def _check_paradox(self, rates: Dict[str, Dict[str, float]]):
        """Check for actual paradox"""
        txs = list(rates.keys())
        if len(txs) < 2: return
        grps = [g for g in rates[txs[0]] if g != 'overall']
        
        better_all = all(rates[txs[0]][g] > rates[txs[1]][g] for g in grps)
        if better_all and rates[txs[0]]['overall'] < rates[txs[1]]['overall']:
            print("\n⚠️ WARNING: Paradox detected!")
            print(f"- {txs[0]} better in subgroups but worse overall")
        else:
            print("\nNote: No paradox, but proportions differ")

if __name__ == "__main__":
    analyzer = SimpsonAnalyzer()
    analyzer.input_data()
    analyzer.analyze()
    
    while input("\nAnalyze another? (y/n): ").lower() == 'y':
        analyzer = SimpsonAnalyzer()
        analyzer.input_data()
        analyzer.analyze()
