using System;
using System.Collections.Generic;

namespace Semana7_Arboles
{
    public class TreeNode<T> where T : IComparable<T>
    {
        public T Value { get; set; }
        public TreeNode<T> Left { get; set; }
        public TreeNode<T> Right { get; set; }

        public TreeNode(T value)
        {
            Value = value;
            Left = null;
            Right = null;
        }
    }

    public class BinarySearchTree<T> where T : IComparable<T>
    {
        public TreeNode<T> Root { get; private set; }

        public void Insert(T value)
        {
            Root = InsertRecursive(Root, value);
        }

        private TreeNode<T> InsertRecursive(TreeNode<T> node, T value)
        {
            if (node == null) return new TreeNode<T>(value);

            int comparison = value.CompareTo(node.Value);
            if (comparison < 0)
                node.Left = InsertRecursive(node.Left, value);
            else if (comparison > 0)
                node.Right = InsertRecursive(node.Right, value);

            return node;
        }

        public bool Search(T value)
        {
            return SearchRecursive(Root, value);
        }

        private bool SearchRecursive(TreeNode<T> node, T value)
        {
            if (node == null) return false;

            int comparison = value.CompareTo(node.Value);
            if (comparison == 0) return true;
            if (comparison < 0) return SearchRecursive(node.Left, value);
            return SearchRecursive(node.Right, value);
        }

        public void Delete(T value)
        {
            Root = DeleteRecursive(Root, value);
        }

        private TreeNode<T> DeleteRecursive(TreeNode<T> node, T value)
        {
            if (node == null) return null;

            int comparison = value.CompareTo(node.Value);
            if (comparison < 0)
                node.Left = DeleteRecursive(node.Left, value);
            else if (comparison > 0)
                node.Right = DeleteRecursive(node.Right, value);
            else
            {
                // Caso 1: Nodo sin hijos
                if (node.Left == null && node.Right == null)
                    return null;

                // Caso 2: Nodo con un hijo
                if (node.Left == null) return node.Right;
                if (node.Right == null) return node.Left;

                // Caso 3: Nodo con dos hijos
                var minRight = FindMin(node.Right);
                node.Value = minRight.Value;
                node.Right = DeleteRecursive(node.Right, minRight.Value);
            }

            return node;
        }

        private TreeNode<T> FindMin(TreeNode<T> node)
        {
            while (node.Left != null)
                node = node.Left;
            return node;
        }

        // Recorrido In-Order (Izquierda-Raíz-Derecha)
        public List<T> InOrder()
        {
            var result = new List<T>();
            InOrderRecursive(Root, result);
            return result;
        }

        private void InOrderRecursive(TreeNode<T> node, List<T> result)
        {
            if (node == null) return;
            InOrderRecursive(node.Left, result);
            result.Add(node.Value);
            InOrderRecursive(node.Right, result);
        }

        // Recorrido Pre-Order (Raíz-Izquierda-Derecha)
        public List<T> PreOrder()
        {
            var result = new List<T>();
            PreOrderRecursive(Root, result);
            return result;
        }

        private void PreOrderRecursive(TreeNode<T> node, List<T> result)
        {
            if (node == null) return;
            result.Add(node.Value);
            PreOrderRecursive(node.Left, result);
            PreOrderRecursive(node.Right, result);
        }

        // Recorrido Post-Order (Izquierda-Derecha-Raíz)
        public List<T> PostOrder()
        {
            var result = new List<T>();
            PostOrderRecursive(Root, result);
            return result;
        }

        private void PostOrderRecursive(TreeNode<T> node, List<T> result)
        {
            if (node == null) return;
            PostOrderRecursive(node.Left, result);
            PostOrderRecursive(node.Right, result);
            result.Add(node.Value);
        }

        public int Height()
        {
            return HeightRecursive(Root);
        }

        private int HeightRecursive(TreeNode<T> node)
        {
            if (node == null) return 0;
            return 1 + Math.Max(HeightRecursive(node.Left), HeightRecursive(node.Right));
        }
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("🌳 Semana 7 - Árboles Binarios de Búsqueda\n");

            var bst = new BinarySearchTree<int>();

            // Insertar elementos
            Console.WriteLine("📥 Insertando elementos: 50, 30, 70, 20, 40, 60, 80");
            var values = new[] { 50, 30, 70, 20, 40, 60, 80 };
            foreach (var val in values)
            {
                bst.Insert(val);
            }

            Console.WriteLine("\n🔍 Recorridos del árbol:");
            Console.WriteLine($"In-Order (ordenado):   {string.Join(", ", bst.InOrder())}");
            Console.WriteLine($"Pre-Order (raíz primero): {string.Join(", ", bst.PreOrder())}");
            Console.WriteLine($"Post-Order (raíz último): {string.Join(", ", bst.PostOrder())}");

            Console.WriteLine($"\n📏 Altura del árbol: {bst.Height()}");

            // Búsquedas
            Console.WriteLine("\n🔎 Búsquedas:");
            Console.WriteLine($"¿Existe 40? {bst.Search(40)}");
            Console.WriteLine($"¿Existe 25? {bst.Search(25)}");
            Console.WriteLine($"¿Existe 70? {bst.Search(70)}");

            // Eliminar elemento
            Console.WriteLine("\n🗑️ Eliminando 30...");
            bst.Delete(30);
            Console.WriteLine($"In-Order después de eliminar: {string.Join(", ", bst.InOrder())}");

            Console.WriteLine("\n🗑️ Eliminando 50 (raíz)...");
            bst.Delete(50);
            Console.WriteLine($"In-Order después de eliminar: {string.Join(", ", bst.InOrder())}");

            Console.WriteLine($"\n📏 Nueva altura: {bst.Height()}");

            Console.WriteLine("\n✅ Programa completado!");
        }
    }
}
