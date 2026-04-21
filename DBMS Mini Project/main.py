import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import crime_crud_op as ops

LOGGED_OFFICER = {"id": None, "name": None}

# ---------------- Login Window ----------------
def show_login_window():
    login_win = tk.Tk()
    login_win.title("Officer Login - Crime Management")
    login_win.geometry("380x220")
    login_win.resizable(False, False)

    tk.Label(login_win, text="Officer Email").pack(pady=(20, 4))
    email_entry = tk.Entry(login_win, width=40)
    email_entry.pack()

    tk.Label(login_win, text="Password").pack(pady=(10, 4))
    pwd_entry = tk.Entry(login_win, width=40, show="*")
    pwd_entry.pack()

    def attempt_login():
        email = email_entry.get().strip()
        pwd = pwd_entry.get().strip()
        if not email or not pwd:
            messagebox.showerror("Error", "Enter email and password.")
            return
        row = ops.authenticate_officer(email, pwd)
        if row:
            LOGGED_OFFICER["id"] = row[0]
            LOGGED_OFFICER["name"] = row[1]
            messagebox.showinfo("Welcome", f"Logged in as Officer {row[1]}")
            login_win.destroy()
            show_dashboard()
        else:
            messagebox.showerror("Access Denied", "Invalid credentials.")

    tk.Button(login_win, text="Login", width=12, command=attempt_login).pack(pady=12)

    login_win.mainloop()

# ---------------- Dashboard ----------------
def show_dashboard():
    root = tk.Tk()
    root.title("Crime Management Dashboard")
    root.geometry("1000x600")

    header = tk.Frame(root)
    header.pack(fill=tk.X, padx=10, pady=6)
    tk.Label(header, text=f"Officer: {LOGGED_OFFICER['name']}", font=("Helvetica", 11, "bold")).pack(side=tk.LEFT)
    tk.Button(header, text="Logout", command=lambda: logout(root)).pack(side=tk.RIGHT)

    search_frame = tk.Frame(root)
    search_frame.pack(fill=tk.X, padx=10, pady=6)
    tk.Label(search_frame, text="Search (type or location):").pack(side=tk.LEFT, padx=(0,6))
    search_var = tk.StringVar()
    search_entry = tk.Entry(search_frame, textvariable=search_var, width=40)
    search_entry.pack(side=tk.LEFT)

    def do_search():
        kw = search_var.get().strip()
        for r in crime_tree.get_children():
            crime_tree.delete(r)
        rows = ops.search_crimes(kw) if kw else ops.get_all_crimes()
        for r in rows:
            crime_tree.insert("", "end", values=(r['id'], r['type'], r['description'][:40], r['date_reported'], r['location'], r.get('status',''), r.get('officer_name','')))

    tk.Button(search_frame, text="Search", command=do_search).pack(side=tk.LEFT, padx=6)
    tk.Button(search_frame, text="Show All", command=lambda: [search_var.set(""), do_search()]).pack(side=tk.LEFT)

    # Treeview for crimes
    cols = ("ID", "Type", "Description", "date_reported", "Location", "Status", "Officer")
    crime_tree = ttk.Treeview(root, columns=cols, show="headings", selectmode="browse")
    for c in cols:
        crime_tree.heading(c, text=c)
        crime_tree.column(c, anchor="w", width=120)
    crime_tree.column("Description", width=300)
    crime_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=6)

    # Fill initial data
    def refresh_list():
        for r in crime_tree.get_children():
            crime_tree.delete(r)
        rows = ops.get_all_crimes()
        for r in rows:
            crime_tree.insert("", "end", values=(r['id'], r['type'], r['description'][:40], r['date_reported'], r['location'], r.get('status',''), r.get('officer_name','')))
    refresh_list()

    btn_frame = tk.Frame(root)
    btn_frame.pack(fill=tk.X, padx=10, pady=6)

    def add_crime_win():
        win = tk.Toplevel(root)
        win.title("Add Crime")
        win.geometry("480x360")
        # fields
        tk.Label(win, text="Type").grid(row=0, column=0, sticky="e", padx=6, pady=6)
        e_type = tk.Entry(win, width=40); e_type.grid(row=0, column=1)
        tk.Label(win, text="Date (YYYY-MM-DD)").grid(row=1, column=0, sticky="e", padx=6, pady=6)
        e_date = tk.Entry(win, width=40); e_date.grid(row=1, column=1)
        tk.Label(win, text="Location").grid(row=2, column=0, sticky="e", padx=6, pady=6)
        e_loc = tk.Entry(win, width=40); e_loc.grid(row=2, column=1)
        tk.Label(win, text="Status").grid(row=3, column=0, sticky="e", padx=6, pady=6)
        e_status = tk.Entry(win, width=40); e_status.grid(row=3, column=1)
        tk.Label(win, text="Description").grid(row=4, column=0, sticky="ne", padx=6, pady=6)
        e_desc = tk.Text(win, width=40, height=6); e_desc.grid(row=4, column=1)

        def save():
            type_ = e_type.get().strip()
            date_ = e_date.get().strip()
            loc = e_loc.get().strip()
            status = e_status.get().strip() or "reported"
            desc = e_desc.get("1.0", "end").strip()
            if not type_:
                messagebox.showerror("Error", "Type is required")
                return
            try:
                ops.add_crime(type_, desc, date_, loc, LOGGED_OFFICER["id"], status)
                messagebox.showinfo("Success", "Crime added")
                win.destroy()
                refresh_list()
            except Exception as ex:
                messagebox.showerror("DB Error", str(ex))

        tk.Button(win, text="Save", command=save).grid(row=5, column=0, columnspan=2, pady=10)

    def get_selected_crime_id():
        sel = crime_tree.selection()
        if not sel:
            messagebox.showerror("Error", "Select a crime first")
            return None
        return crime_tree.item(sel)['values'][0]

    def edit_crime_win():
        cid = get_selected_crime_id()
        if not cid:
            return
        data = ops.get_crime_by_id(cid)
        if not data:
            messagebox.showerror("Error", "Crime not found")
            return

        win = tk.Toplevel(root)
        win.title("Edit Crime")
        win.geometry("480x360")
        tk.Label(win, text="Type").grid(row=0, column=0, sticky="e", padx=6, pady=6)
        e_type = tk.Entry(win, width=40); e_type.grid(row=0, column=1); e_type.insert(0, data.get('type',''))
        tk.Label(win, text="Date (YYYY-MM-DD)").grid(row=1, column=0, sticky="e", padx=6, pady=6)
        e_date = tk.Entry(win, width=40); e_date.grid(row=1, column=1); e_date.insert(0, str(data.get('date_reported') or ""))
        tk.Label(win, text="Location").grid(row=2, column=0, sticky="e", padx=6, pady=6)
        e_loc = tk.Entry(win, width=40); e_loc.grid(row=2, column=1); e_loc.insert(0, data.get('location',''))
        tk.Label(win, text="Status").grid(row=3, column=0, sticky="e", padx=6, pady=6)
        e_status = tk.Entry(win, width=40); e_status.grid(row=3, column=1); e_status.insert(0, data.get('status',''))
        tk.Label(win, text="Description").grid(row=4, column=0, sticky="ne", padx=6, pady=6)
        e_desc = tk.Text(win, width=40, height=6); e_desc.grid(row=4, column=1); e_desc.insert("1.0", data.get('description',''))

        def save_edit():
            try:
                updated = ops.update_crime(cid, e_type.get().strip(), e_desc.get("1.0","end").strip(), e_date.get().strip(), e_loc.get().strip(), e_status.get().strip())
                if updated:
                    messagebox.showinfo("Success", "Crime updated")
                    win.destroy()
                    refresh_list()
                else:
                    messagebox.showwarning("No Change", "No rows updated")
            except Exception as ex:
                messagebox.showerror("DB Error", str(ex))

        tk.Button(win, text="Save Changes", command=save_edit).grid(row=5, column=0, columnspan=2, pady=10)

    def delete_crime_action():
        cid = get_selected_crime_id()
        if not cid:
            return
        if messagebox.askyesno("Confirm", "Delete selected crime and its child records?"):
            try:
                ok = ops.delete_crime(cid)
                if ok:
                    messagebox.showinfo("Deleted", "Crime deleted")
                    refresh_list()
                else:
                    messagebox.showwarning("Failed", "Delete failed or not found")
            except Exception as ex:
                messagebox.showerror("DB Error", str(ex))

    def view_details():
        cid = get_selected_crime_id()
        if not cid:
            return
        data = ops.get_crime_by_id(cid)
        if not data:
            messagebox.showerror("Error", "Crime not found")
            return

        win = tk.Toplevel(root)
        win.title(f"Crime Details - ID {cid}")
        win.geometry("900x600")

        # Top: crime info
        topf = tk.Frame(win); topf.pack(fill=tk.X, padx=8, pady=6)
        tk.Label(topf, text=f"Type: {data.get('type','')}").pack(anchor="w")
        tk.Label(topf, text=f"date_reported: {data.get('date_reported','')}").pack(anchor="w")
        tk.Label(topf, text=f"Location: {data.get('location','')}").pack(anchor="w")
        tk.Label(topf, text=f"Status: {data.get('status','')}").pack(anchor="w")
        tk.Label(topf, text="Description:").pack(anchor="w")
        tk.Label(topf, text=data.get('description',''), wraplength=880, justify="left").pack(anchor="w", pady=(0,6))

        notebook = ttk.Notebook(win)
        notebook.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)

        # Witnesses tab
        wtab = ttk.Frame(notebook); notebook.add(wtab, text="Witnesses")
        wtree = ttk.Treeview(wtab, columns=("ID","Witness Name","Statement", "User ID"), show="headings")
        for c in ("ID","Witness Name","Statement", "User ID"):
            wtree.heading(c, text=c)
        wtree.column("Statement", width=400)
        wtree.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        def load_witnesses():
            for i in wtree.get_children(): wtree.delete(i)
            for w in ops.get_witnesses_for_crime(cid):
                wtree.insert("", "end", values=(w['id'], w['witness_name'], w['statement'], w['user_id']))
        load_witnesses()

        def add_witness_win():
            user_id = simpledialog.askinteger("Witness", "User ID (if known):", parent=win, minvalue=1)
            if not user_id: return
            witness_name = simpledialog.askstring("Witness", "Witness Name:", parent=win)
            if not witness_name: return
            statement = simpledialog.askstring("Witness", "Statement:", parent=win)
            if statement is None: return
            try:
                ops.add_witness(cid, user_id, witness_name, statement)
                load_witnesses()
            except Exception as ex:
                messagebox.showerror("DB Error", str(ex))

        def delete_witness_action():
            sel = wtree.selection()
            if not sel:
                messagebox.showerror("Error", "Select witness")
                return
            wid = wtree.item(sel)['values'][0]
            if messagebox.askyesno("Confirm", "Delete witness?"):
                try:
                    ops.delete_witness(wid)
                    load_witnesses()
                except Exception as ex:
                    messagebox.showerror("DB Error", str(ex))

        tk.Button(wtab, text="Add Witness", command=add_witness_win).pack(side=tk.LEFT, padx=6, pady=6)
        tk.Button(wtab, text="Delete Witness", command=delete_witness_action).pack(side=tk.LEFT, padx=6, pady=6)

        # Suspects tab
        stab = ttk.Frame(notebook); notebook.add(stab, text="Suspects")
        stree = ttk.Treeview(stab, columns=("ID","Name","Description"), show="headings")
        for c in ("ID","Name","Description"):
            stree.heading(c, text=c)
        stree.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        def load_suspects():
            for i in stree.get_children(): stree.delete(i)
            for s in ops.get_suspects_for_crime(cid):
                stree.insert("", "end", values=(s['id'], s['name'], s.get('description','')))
        load_suspects()

        def add_suspect_win():
            name = simpledialog.askstring("Suspect", "Name:", parent=win)
            if not name: return
            description = simpledialog.askstring("Suspect", "Description:", parent=win)
            if description is None: return
            try:
                ops.add_suspect(cid, name, description)
                load_suspects()
            except Exception as ex:
                messagebox.showerror("DB Error", str(ex))

        def delete_suspect_action():
            sel = stree.selection()
            if not sel:
                messagebox.showerror("Error", "Select suspect")
                return
            sid = stree.item(sel)['values'][0]
            if messagebox.askyesno("Confirm", "Delete suspect?"):
                try:
                    ops.delete_suspect(sid)
                    load_suspects()
                except Exception as ex:
                    messagebox.showerror("DB Error", str(ex))

        tk.Button(stab, text="Add Suspect", command=add_suspect_win).pack(side=tk.LEFT, padx=6, pady=6)
        tk.Button(stab, text="Delete Suspect", command=delete_suspect_action).pack(side=tk.LEFT, padx=6, pady=6)

        # Evidence tab
        etab = ttk.Frame(notebook); notebook.add(etab, text="Evidence")
        etree = ttk.Treeview(etab, columns=("ID","Description", "Location Found", "Date Found"), show="headings")
        for c in ("ID","Description", "Location Found", "Date Found"):
            etree.heading(c, text=c)
        etree.column("Description", width=300)
        etree.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        def load_evidence():
            for i in etree.get_children(): etree.delete(i)
            for e in ops.get_evidence_for_crime(cid):
                etree.insert("", "end", values=(e['evidence_id'], e.get('description',''), e.get('location_found',''), e.get('date_found','')))
        load_evidence()

        def add_evidence_win():
            location_found = simpledialog.askstring("Evidence", "Location Found:", parent=win)
            if not location_found: return
            date_found = simpledialog.askstring("Evidence", "Date Found (YYYY-MM-DD):", parent=win)
            if date_found is None: return # Allow empty date string
            desc = simpledialog.askstring("Evidence", "Description:", parent=win)
            if desc is None: return
            try:
                ops.add_evidence(cid, desc, location_found, date_found)
                load_evidence()
            except Exception as ex:
                messagebox.showerror("DB Error", str(ex))

        def delete_evidence_action():
            sel = etree.selection()
            if not sel:
                messagebox.showerror("Error", "Select evidence")
                return
            eid = etree.item(sel)['values'][0]
            if messagebox.askyesno("Confirm", "Delete evidence?"):
                try:
                    ops.delete_evidence(eid)
                    load_evidence()
                except Exception as ex:
                    messagebox.showerror("DB Error", str(ex))

        tk.Button(etab, text="Add Evidence", command=add_evidence_win).pack(side=tk.LEFT, padx=6, pady=6)
        tk.Button(etab, text="Delete Evidence", command=delete_evidence_action).pack(side=tk.LEFT, padx=6, pady=6)

    tk.Button(btn_frame, text="Add Crime", width=14, command=add_crime_win).pack(side=tk.LEFT, padx=6)
    tk.Button(btn_frame, text="Edit Selected", width=14, command=edit_crime_win).pack(side=tk.LEFT, padx=6)
    tk.Button(btn_frame, text="Delete Selected", width=14, command=delete_crime_action).pack(side=tk.LEFT, padx=6)
    tk.Button(btn_frame, text="View Details", width=14, command=view_details).pack(side=tk.LEFT, padx=6)

    root.mainloop()

def logout(win):
    if messagebox.askyesno("Logout", "Logout and return to login?"):
        win.destroy()
        # reset global
        LOGGED_OFFICER["id"] = None
        LOGGED_OFFICER["name"] = None
        show_login_window()

if __name__ == "__main__":
    show_login_window()