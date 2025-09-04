// Alpine.js components and utilities

// Formula Manager Component
document.addEventListener('alpine:init', () => {
    Alpine.data('formulaManager', () => ({
        selectedFormulas: [],
        exportFormat: 'csv',
        
        toggleFormula(formulaId) {
            const index = this.selectedFormulas.indexOf(formulaId);
            if (index > -1) {
                this.selectedFormulas.splice(index, 1);
            } else {
                this.selectedFormulas.push(formulaId);
            }
        },
        
        selectAll() {
            const checkboxes = document.querySelectorAll('.formula-checkbox');
            this.selectedFormulas = Array.from(checkboxes).map(cb => parseInt(cb.value));
        },
        
        deselectAll() {
            this.selectedFormulas = [];
        },
        
        exportSelected() {
            if (this.selectedFormulas.length === 0) {
                alert('Please select at least one formula to export');
                return;
            }
            
            // Trigger export endpoint
            const params = new URLSearchParams({
                ids: this.selectedFormulas.join(','),
                format: this.exportFormat
            });
            
            window.location.href = `/api/export?${params}`;
        }
    }));
    
    // Search Enhancement Component
    Alpine.data('searchEnhanced', () => ({
        recentSearches: JSON.parse(localStorage.getItem('recentSearches') || '[]'),
        favorites: JSON.parse(localStorage.getItem('favoriteFormulas') || '[]'),
        
        addToRecent(searchTerm) {
            if (!searchTerm) return;
            
            this.recentSearches = this.recentSearches.filter(s => s !== searchTerm);
            this.recentSearches.unshift(searchTerm);
            this.recentSearches = this.recentSearches.slice(0, 5);
            localStorage.setItem('recentSearches', JSON.stringify(this.recentSearches));
        },
        
        toggleFavorite(formulaId) {
            const index = this.favorites.indexOf(formulaId);
            if (index > -1) {
                this.favorites.splice(index, 1);
            } else {
                this.favorites.push(formulaId);
            }
            localStorage.setItem('favoriteFormulas', JSON.stringify(this.favorites));
        },
        
        isFavorite(formulaId) {
            return this.favorites.includes(formulaId);
        },
        
        clearRecent() {
            this.recentSearches = [];
            localStorage.removeItem('recentSearches');
        }
    }));
});

// HTMX Event Handlers
document.body.addEventListener('htmx:afterSwap', (event) => {
    // Reinitialize any components after HTMX swap
    if (event.detail.target.id === 'search-results') {
        // Trigger Alpine to update
        Alpine.nextTick(() => {
            // Any post-swap initialization
        });
    }
});

// Copy to clipboard utility
window.copyToClipboard = async (text, buttonElement) => {
    try {
        await navigator.clipboard.writeText(text);
        const originalText = buttonElement.innerText;
        buttonElement.innerText = 'Copied!';
        buttonElement.classList.add('text-green-600');
        
        setTimeout(() => {
            buttonElement.innerText = originalText;
            buttonElement.classList.remove('text-green-600');
        }, 2000);
    } catch (err) {
        console.error('Failed to copy:', err);
    }
};